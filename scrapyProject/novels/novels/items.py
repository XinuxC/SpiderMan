# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()  #小说名
    title = scrapy.Field()  # 章节名
    body = scrapy.Field()  # 正文
    order_id = scrapy.Field()  # 排序用ID

