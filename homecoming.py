#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : homecoming.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/9/27
# @Desc  :


import urllib.request

import requests
# url='https://www.douban.com/'
# req = requests.get(url)
# print(type(req))
# print(req.url)
# print(req.encoding)
# print(req.status_code)
# print(req.text)
# print(req.content)

# 定义保存函数

def saveFile(data):
    path = "douban.html"
    f = open(path, 'w',encoding='utf-8')
    f.write(data)
    f.close()


# 网址
url = "https://www.douban.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=url, headers=headers)

print(req.encoding)

data = req.text
print(type(data))
# 也可以把爬取的内容保存到文件中
saveFile(data)

# 打印抓取的内容
print(data)

# 打印爬取网页的各类信息
print(type(req))
print(req.url)
print(req.status_code)