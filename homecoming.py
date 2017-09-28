#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : homecoming.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/9/27
# @Desc  : 抓取豆瓣首页和首页图片


import urllib.request

import re
import os
import requests


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
print(req.raise_for_status)
# print(req.content)
# print(req.text)

data = req.text
# print(type(data))
# 也可以把爬取的内容保存到文件中
saveFile(data)
#
# # 打印抓取的内容
# print(data)
#
# # 打印爬取网页的各类信息
# print(type(req))
# print(req.url)
# print(req.status_code)


#s='https://img1.doubanio.com/view/photo/albumcover/public/p2456421058.webp'
#s='https://img1.doubanio.com/view/dianpu_product_item/medium/public/p1982227.jpg'
#s='https://img1.doubanio.com/view/site/small/public/fc00cb95a9b74d9.jpg'
#s='https://img3.doubanio.com/view/site/small/public/8b5b390e6ffe23d.jpg'
#s='https://img3.doubanio.com/spic/s29551782.jpg'
#s='https://img3.doubanio.com/img/songlist/large/371319-2.jpg'

pattern=r'https://img\d.doubanio.com/\w{3,4}/.*?.jpg|webp'
pattern1=r'(https:[^s]*?.jpg)|(https:[^s]*?.webp)'
result=re.findall(pattern,req.text)
# print(result)

def savePics(name,data):
    dirpath='.\\doubanpics'
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    filename=os.path.join(dirpath,name)
    with open(filename,'wb') as f :
        f.write(data)

for pic in result:
    # print(pic)
    res = requests.get(pic)
    data = res.content
    name = pic.rpartition('/')[-1]
    # savePics(name,data)
print(type(data))
print(type(res.text))




