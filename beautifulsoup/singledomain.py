#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : singledomain.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/17
# @Desc  : 遍历单个域名 实现"维基百科六度分隔理论",从埃里克埃德尔的词条页面开始,经过最少的链接点击数找到凯文贝肯的词条页面
import random
import re

import datetime
import requests
from bs4 import BeautifulSoup
proxies = {
        "http": "117.90.0.225:9000",
        "http": "186.154.146.26:8080",
        "http": "175.155.25.27:808",
        "http": "124.88.67.52:843",
        "http": "119.5.0.7:808"
        }


url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
r = requests.get(url=url)
bsObj = BeautifulSoup(r.text,"html.parser")
# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])  # 包含了我们不需要的链接,
# 发现指向词条页面的链接有三个共同特点1.都在id是bodyContent的div标签里;2.url链接不包含冒号;3.URL链接都以/wiki/开头

#修改代码
# for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a"
#         ,href = re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

random.seed(datetime.datetime.now())  # 用系统当前时间生成一个随机数生成器,保证每次运行时,维基百科词条的选择都是一个全新的随机路径

def getLinks(articleUrl):
    r = requests.get("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(r.text,"html.parser")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a"
        ,href = re.compile("^(/wiki/)((?!:).)*$"))
# 先把从起始页面凯文贝肯里的词条链接列表(links变量)设置成链接列表
links = getLinks("/wiki/Kevin_Bacon")
# 然后用一个循环,从页面中随机找出一个词条链接并抽取href属性,打印这个页面链接,再传入getLink函数,重新获取链接列表
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)