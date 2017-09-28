#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zhihu.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/28
# @Desc  :


import requests

url='https://www.zhihu.com/'

data={
    # '_xsrf':	'2c7a99e08f2443bd1bce9fa3c8a87cae',
    'password' : 'yaojing0129',
    'captcha' :{'img_size':[200,44],'input_points':[[43.8,23.2],[106.8,27.2]]},
    'captcha_type' : 'cn',
    'phone_num' :'18200590129',
    }
headers = {'Host': 'www.zhihu.com',
'Connection': 'keep-alive',
'Content-Length': '215',
'Accept': '*/*',
'Origin': 'https://www.zhihu.com',
'X-Requested-With': 'XMLHttpRequest',
'X-Xsrftoken': '2c7a99e08f2443bd1bce9fa3c8a87cae',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'https://www.zhihu.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8'
           }

r=requests.get(url,headers)
print(r.status_code)