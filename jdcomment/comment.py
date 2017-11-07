#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : comment.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/7
# @Desc  :


import re
import requests
import pandas as pd
import csv

url = 'https://sclub.jd.com/comment/productPageComments.action' \
      '?callback=fetchJSON_comment98vv2605&productId=5089235&score=0&sortType=5&page=%d' \
      '&pageSize=10&isShadowSku=0&rid=0&fold=1' % 1

r = requests.get(url)
print(r.encoding)
html = r.text

print(type(html))

f = open('comment.txt','a',encoding='utf-8')
p = re.compile(r'"content":"(.*?)","')
comments = p.findall(html)
print(type(comments))
for index , comment in enumerate(comments):
    comment = comment.replace('\\n','')
    # print(index,':',comment)
    f.write(str(index))
    f.write(':')
    f.write(comment)
    f.write('\n')
f.close()
# header = ['index','content']
# with open('comment.csv','w+',encoding='GBK') as f :
#     f_csv = csv.writer(f)
#     f_csv.writerow(header)
#     p = re.compile(r'"content":"(.*?)","')
#     comments = p.findall(html)
#     print(type(comments))
#     for index , comment in enumerate(comments):
#         comment = comment.replace('\\n','')
#         f_csv.writerow(str(index))
#         f_csv.writerow(comment)