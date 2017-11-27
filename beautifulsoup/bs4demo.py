#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bs4demo.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/27
# @Desc  :

import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
bsObj = BeautifulSoup(html_doc,"lxml")

# print(bsObj.strings)
# print(bsObj.head.string)
print(bsObj.title)
print(bsObj.title.string)
# print(bsObj.title.get_text())  # 和.string作用相同

#all the links in tag a
for link in bsObj.find_all("a"):
    print(link.get('href'))
    # print(link['href'])
    # print(link.attrs)


# import re
# for link in bsObj.find_all(id=re.compile('link\d')):
#     print(link['href'])


# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# print(bsObj.find_all(has_class_but_no_id))


# def not_lacie(href):
#     return href and not re.compile("lacie").search(href)
#
# print(bsObj.find_all(href=not_lacie))

#
# print(bsObj.select("html head title")[0].get_text())
#
# print(bsObj.select('[class="sister"]'))


