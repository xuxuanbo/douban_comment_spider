# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import MySQLdb
class DoubancommentPipeline(object):
    def send_data_to_database(self):
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
    def process_item(self, item, spider):
        # 获取当前工作目录
        # base_dir = os.getcwd()
        # json_src = base_dir + '/comment'+item['name'].encode('utf-8')+'.json'
        # with open(json_src, 'a') as f:
        #     json.dump(dict(item),f,indent=4)
        conn = MySQLdb.connect(host='localhost', user='root', passwd='1601', db='TEST', charset="utf8")
        cur = conn.cursor()
        cur.execute("insert into douban_comment (movie_id,uid,comment_type,time,score,content,like_num) values (" + item[
            'id'] + ",\'" + item['user_url'].split("/")[-2] + "\',\'" + item['type'] + "\',\'" + item['comment_time'] + "\',\'" + item['rating'] + "\',\'" +item['content'] + "\',\'" + item['votes'] + "\')")
        conn.commit()
        print item['name']
        return item
