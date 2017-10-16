#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : navigatingTree.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/15
# @Desc  : HTML 导航树的纵向和横向导航
import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'

html = requests.get(url)
bsObj = BeautifulSoup(html.text,'html.parser')

# '''.children():找出子标签'''
# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)
# '''.descendants():后代标签'''
# for descendants in bsObj.find("table",{"id":"giftList"}).descendants:
#     print(descendants)

'''处理兄弟标签next_siblings():可以让收集表格数据很简单,尤其处理带标题行的表格'''
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
    # 1.对象不能把自己作为兄弟标签,任何时候获取一个标签的兄弟标签,都不会包含自己
    # 2.这个函数只调用后面的兄弟标签
'''previous_siblings()找到前面的兄弟标签'''
'''next_sibling和previous_sibling函数返回单个标签,而不是一组标签'''

'''父标签处理parent和parents函数'''
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

for imgsrc in bsObj.findAll('img'):
    print(imgsrc.attrs['src'])
