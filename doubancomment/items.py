# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubancommentItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    votes = scrapy.Field()
    comment_info = scrapy.Field()
    user_name = scrapy.Field()
    user_url = scrapy.Field()
    type = scrapy.Field()
    rating = scrapy.Field()
    comment_time = scrapy.Field()
    content = scrapy.Field()
    comment_type = scrapy.Field()
    # name = scrapy.Field()
    pass
