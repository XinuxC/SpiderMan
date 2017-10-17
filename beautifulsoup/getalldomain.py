#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : getalldomain.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/17
# @Desc  : 采集整个网站

#1.生成网站地图;2.收集数据

'''一个常用的费时的网站采集方法就是从顶级页面开始,然后搜索页面上的所有链接,形成列表
再去采集这些链接的每一个页面,然后把每个页面上找到的链接形成新的列表,重复下一轮采集
为避免重复采集,链接去重很重要,把已发现的所有链接都放到一起,保存在方便查询的列表里(set集合),只有新链接会被采集,
再从其他页面中搜索其他链接
'''

import  requests
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global  pages
    r = requests.get("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(r.text,"html.parser")
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:  # 新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")