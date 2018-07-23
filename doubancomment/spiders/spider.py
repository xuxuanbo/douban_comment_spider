# -*- coding: utf-8 -*-
import scrapy
from doubancomment.items import DoubancommentItem
from scrapy.selector import Selector
from scrapy import log
from scrapy.http import Request,FormRequest
import MySQLdb
import json
# import doubancomment.settings
class LessionSpider(scrapy.Spider):
    name = 'see'
    headers = {
    "Host":"www.douban.com",
    "Referer":"https://accounts.douban.com/login?redir=https://www.douban.com/doumail/&source=None&login_type=sms",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}
    def start_requests(self):
        yield scrapy.Request(url="https://accounts.douban.com/login?source=movie", callback=self.login,dont_filter = True,meta={ 'cookiejar':1 ,
                'data': {
                }
            })
    def login(self,response):
        print ('Preparing login')
        sel = Selector(response)
        nodes = sel.xpath("//*[@class='captcha_image']/@src").extract()
        if nodes :
            print (nodes)
            xerf = raw_input()
            return scrapy.FormRequest.from_response(

            response,
            formdata={
                      'captcha-solution': xerf,
                      'form_email': '747561582@qq.com',
                      'form_password': '*********'
            },
            callback=self.after_login,meta=response.meta,
            )

        return scrapy.FormRequest.from_response(
                response,
                formdata={'form_email': '747561582@qq.com',
                          'form_password': '*********'
                        },
                callback=self.after_login,meta=response.meta,
        )
    def get_data_from_database(self):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='1601', db='TEST', charset="utf8")
        cur = conn.cursor()
        cur.execute("select * from movie")
        item = cur.fetchone()
        i = 0
        classifications = {}
        while item != None:
            i+=1
            if i > 10:
                break
            classifications.update({item[0]:item[1]})
            item = cur.fetchone()
        return classifications
    def after_login(self,response):
        #check login succeed before going on
        if "authentication failed" in response.body:
            self.log("login failed", level = log.ERROR)
        # cookies_list = response.request.headers.getlist('Cookie')
        # cookies_dict = {}
        # for i in cookies_list:
        #     list1 = i.split(";")
        #     for j in list1:
        #         list2 = j.split("=")
        #         cookies_dict.update({list2[0].replace(" ",""):list2[1]})
        # print cookies_dict
        classifications = self.get_data_from_database()
        # response.meta['data'].update({'name': None, 'year': None})
        for classification, year in classifications.items():
            # print classification+'!!!!!!!!'+year
            data = {}
            data.update(response.meta)
            data.update({'name':classification,'year':year})
            yield scrapy.Request(url='https://movie.douban.com/j/subject_suggest?q=' + classification, callback=self.after_post,
                                 dont_filter=True, meta=data)

    def after_post(self,response):
        sites = json.loads(response.body_as_unicode())
        for i in sites:
            i = dict(i)
            print i['year']
            if i['year'] == response.meta['year']:
                yield scrapy.Request(url=i['url'].split("?")[0],callback=self.redirect, dont_filter=True, meta=response.meta)
                return
    def redirect(self,response):
        data = {}
        data.update(response.meta)
        data.update({'id': response.url.split("/")[-2]})
        yield scrapy.Request(url=response.url+"/comments?start=0&limit=20&sort=new_score&status=P&percent_type=", callback=self.parse, dont_filter=True, meta=data)
        yield scrapy.Request(url=response.url+"comments?start=0&limit=20&sort=new_score&status=P&percent_type=h", callback=self.parse, dont_filter=True, meta=data)
        yield scrapy.Request(url=response.url+"/comments?start=0&limit=20&sort=new_score&status=P&percent_type=m", callback=self.parse, dont_filter=True, meta=data)
        yield scrapy.Request(url=response.url+"/comments?start=0&limit=20&sort=new_score&status=P&percent_type=l", callback=self.parse, dont_filter=True, meta=data)
        yield scrapy.Request(url=response.url+"/comments?status=F", callback=self.parse, dont_filter=True, meta=data)
    def parse(self, response):
        comment_type = response.url
        comment_item=response.xpath("//div[@id='comments']//div[@class='comment-item']")
        name = response.xpath("//h1/text()").extract_first().encode('utf-8').replace(" 短评","")
        for i in comment_item:
            votes = i.xpath(".//span[@class='votes']//text()").extract_first()
            comment_info = i.xpath(".//span[@class='comment-info']")
            user_name = comment_info.xpath(".//a/text()").extract_first()
            user_url = comment_info.xpath(".//a/@href").extract_first()
            type = comment_info.xpath(".//span//text()").extract_first()
            if comment_info.xpath(".//span[contains(@class,'allstar')]/@class").extract_first() != None:
                rating = comment_info.xpath(".//span[contains(@class,'allstar')]/@class").extract_first().replace("allstar", "").replace(
                " rating", "")
            else:
                rating = 'None'
            comment_time = comment_info.xpath(".//span[@class='comment-time ']/@title").extract_first().split(" ")[0]
            # print votes, user_name, user_url, type, rating, comment_time
            content = i.xpath(".//p[@class='']//text()").extract_first()
            # print content
            data = {}
            data['id'] = response.meta['id']
            data['votes'] = votes
            data['user_name'] = user_name
            data['user_url'] = user_url
            data['rating'] = rating
            data['type'] = type
            data['comment_time'] = comment_time
            data['content'] = content
            data['name'] = response.meta['name']
            # print data
            yield DoubancommentItem(data)
        if response.xpath("//*[@class='next']/@href").extract_first() == None:
            print response.xpath("//*[@class='next']").extract_first()
            return
        else :
            url = response.url.split("?")[0]
            url += response.xpath("//*[@class='next']/@href").extract_first()
            yield scrapy.Request(url=url, callback=self.parse,dont_filter = True,meta=response.meta)

