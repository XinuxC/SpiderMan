#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : meetbs4.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/12
# @Desc  :

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#Section 1 first meet BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page1.html'
# html = urlopen(url)
# print(type(html))
# # print(type(html.read()))
# bsObj = BeautifulSoup(html.read(),'html.parser')
# print(bsObj)
# #提取标签
# print(bsObj.h1)
# print(bsObj.html.head.title)
# print(bsObj.html.body.div)

#可靠的连接
def getTile(url):
    #如果获取网页的时候遇到问题返回一个None对象,则抛出HTTPError
    try:
        html = urlopen(url)
    except HTTPError as e :
        return None
    #如果获取标签出错,抛出AttributeError
    try:
        bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.body.h1
    except AttributeError as e :
        return None
    return title
title = getTile(url)
if title == None:
    print('Title could not be found')
else:
    print(title)


if __name__ == '__main__':
    getTile(url)
