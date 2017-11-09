#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/9
# @Desc  :
import re

import requests

'https://github.com/xchaoinfo/fuck-login'
headers = {
    # 'Host' : 'login.sina.com.cn',
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',

}

url = 'https://passport.weibo.cn/signin/login'
post_data = {

    'capId' : 'yao_jing_0129@hotmail.com',
    'password' : 'yaojing900129'
}


session = requests.Session()
# r = session.post(url=url,headers=headers,data=post_data)
# r.encoding='gb2312'
# # print(r.text)
# html = session.get('https://m.weibo.com')
# html.encoding='gb2312'
# print(html.text)
url_login = 'http://service.weibo.com/widget/widget_blog.php?uid=1949428041'
html = session.get(url_login, headers=headers)
print(html.encoding)
html.encoding='utf-8'
print(html.text)
