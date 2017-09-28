#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zhihu.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/28
# @Desc  :


import requests

# url='https://www.zhihu.com/login/email'
#
# login_data={
#     '_xsrf': '33383531316231362d363736662d343161382d383833622d376438373239633233393237',
#     'password' : 'yaojing0129',
#     'remember_me': 'true',
#      'email': 'pishit2009@gmail.com',
#     }
# headers = { 'Host': 'www.zhihu.com',
#             'Connection': 'keep-alive',
#             'Content-Length': '215',
#             'Accept': '*/*',
#             'Origin': 'https://www.zhihu.com',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#             'Referer': 'https://www.zhihu.com/',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Accept-Language': 'zh-CN,zh;q=0.8'
#            }
#
# s=requests.session()
# r=s.post(url,headers,login_data)
# print(r.status_code)
# print(r.text)

import requests
import re

def getContent(url):
#使用requests.get获取知乎首页的内容
    r = requests.get(url)
#request.get().content是爬到的网页的全部内容
    return r.content

#获取_xsrf标签的值
def getXSRF(url):
#获取知乎首页的内容
    content = getContent(url)
#正则表达式的匹配模式
    pattern = re.compile(r'.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?')
#re.findall查找所有匹配的字符串
    match = re.findall(pattern, content)
    xsrf = match[0]
#返回_xsrf的值
    return xsrf

#登录的主方法
def login(baseurl,email,password):
#post需要的表单数据，类型为字典
    login_data = {
            '_xsrf': getXSRF(baseurl),
            'password': password,
            'remember_me': 'true',
            'email': email,
    }
#设置头信息
    headers_base = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        'Referer': 'http://www.zhihu.com/',
    }
#使用seesion登录，这样的好处是可以在接下来的访问中可以保留登录信息
    session = requests.session()
#登录的URL
    baseurl += "/login/email"
#requests 的session登录，以post方式，参数分别为url、headers、data
    content = session.post(baseurl, headers = headers_base, data = login_data)
#成功登录后输出为 {"r":0,
#"msg": "\u767b\u9646\u6210\u529f"
#}
    print(content.text)
#再次使用session以get去访问知乎首页，一定要设置verify = False，否则会访问失败
    s = session.get("http://www.zhihu.com", verify = False)
    print(s.text.encode('utf-8'))
#把爬下来的知乎首页写到文本中
    f = open('zhihu.txt', 'w')
    f.write(s.text.encode('utf-8'))

url = "http://www.zhihu.com"
#进行登录，将星号替换成你的知乎登录邮箱和密码即可
login(url,"pishit2009@gmail.com","yaojing0129")