#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : douban_movie250.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/8
# @Desc  : xpath 的使用



import requests
from lxml import etree
session = requests.Session()
for id in range(0,250,25):
    url = 'https://movie.douban.com/top250?start=' + str(id)
    r = session.get(url)
    r.encoding = 'utf-8'
    root = etree.HTML(r.content)
    items  = root.xpath('//ol/li/div[@class="item"]')
    # print(len(items))
    for item in items:
        title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')[0]
        cast = item.xpath('./div[@class="info"]//p/text()')[0].strip()
        star = item.xpath('./div[@class="info"]//span[@class="rating_num"]/text()')[0]
        try:
            inq = item.xpath('./div[@class="info"]//p/span[@class="inq"]/text()')[0]
            if len(inq) >0:
                print('片名:%s\t豆瓣评分%s\t%s\tQuote:%s' % (title, star, cast, inq))
        except:
            print('片名:%s\t豆瓣评分%s\t%s\tQuote:None'% (title,star,cast))
