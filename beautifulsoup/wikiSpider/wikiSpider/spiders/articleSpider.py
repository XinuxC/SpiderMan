#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : articleSpider.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/23
# @Desc  : scrapy 大幅降低网页链接查找和识别工作复杂度,可以轻松采集一个或多个域名的信息


from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page','https://en.wikipedia.org/wiki/Python_%28programming_language%29']

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text() ')[0].extract()
        print('title is : '+title)
        item['title'] = title
        return item
