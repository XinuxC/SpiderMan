#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : headtobs4.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/12
# @Desc  :
from urllib.request import urlopen
import requests
from bs4 import  BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
r = requests.get(url)
print(type(r.text))
# print(r.status_code)
print(r.encoding)
r.encoding='utf-8'
print(r.encoding)
# with open('warandpeacd.html','w') as f :
#     f.write(r.text)
bsObj = BeautifulSoup(r.text,"html.parser")
#findAll[find_all()?]函数抽取只包含在<span class="green"></span>标签里的文字
nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    # .get_text()会把HTML文档中所有的标签(超链接,段落,标签)都清除,返回一个只包含文字的字符串
    print(name.get_text())
# 以前urllib.request的实现方法
# r = urlopen(url)
# print(type(r))
# bsObj = BeautifulSoup(r,"html.parser")
# nameList = bsObj.findAll("span",{"class":"green"})
# for name in nameList:
#     print(name.get_text())

#返回html中标题标签列表
tagList = bsObj.find_all({'h1','h2','span'})
# for tag in tagList:
#     print(tag)

#返回html中红色与绿色的span标签
spanTag = bsObj.find_all({"span":{"green","red"}})
# for st in spanTag:
#     print(st)

''' 
 find()和findAll()[find_all()?]
    bsObj.find(tag='',attrs='',recursive=True,text='',keywords='')
    bsObj.find_all(tag='',attrs='',recursive=True,text='',limit='',keywords='')
1.tag和attributes最常用
2.recursive是个布尔变量,默认为True,查找标签参数的所有子标签;False,只查找文档的一级标签
3.text 用标签的文本内容去匹配,如nameList = bsObj.findAll(text='the prince')
4.limit 只用于findAll,如果只想获取前N项结果,可以设置,但是顺序是按照网页上的顺序,未必是想要的;
    find 等价于findAll的limit等于1的情形
5.keyword,可以选择那些具有指定标签的属性,例如
    allText = bsObj.findAll(id = "text") 和allText = bsObj.findAll("",{"id" = "text"})完全一样
    print(allText[0].get_text())
    在使用class的时候,因为是关键字,所以如下使用
    allText = bsObj.findAll(class_="green") 或者allText = bsObj.findAll("",{"class" = "green"})
    print(allText[0].get_text())
'''

"""
其他BeautifulSoup对象
BeautifulSoup对象
 前面的bsObj
标签Tag对象
 通过find和findAll,或者直接调用子标签获取的一列对象或单个对象,如bsObj.div.h1
另外两个不常用对象
 NavigableString对象:用来表示标签里的文字,不是标签
 Comment对象:用来查找html文档的注释标签,像<!--注释-->  
"""
