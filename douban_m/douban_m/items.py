# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMItem(scrapy.Item):
    # define the fields for your item here like:
    score = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    zan = scrapy.Field()
    buzan = scrapy.Field()
