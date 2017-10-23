# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


# scrapy 的每个Item(条目)对象表示网站上的一个页面,当然 也可以根据需要定义不同的条目(比如url,content,header,image等)
# 现在只演示收集每页的title字段(field)
import scrapy
from scrapy import Item,Field


class WikispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Article(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
