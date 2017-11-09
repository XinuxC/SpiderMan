#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/9
# @Desc  :


import json
import time

import requests
from bs4 import BeautifulSoup

#使用requests.session保持一个session,方便cookie操作
session = requests.session()

#从txt文件中获取cookies,json->dict存入session.cookies
with open("cookies.txt",'r') as f:
    cookies = json.load(f)
session.cookies.update(cookies)

#默认headers模拟浏览器请求
headers = {
    "Host": "www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
}

#获取xsrf值,用于登录表单提交
def get_xsrf():
    response = session.get("https://www.zhihu.com",headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    value = soup.find('input',attrs={"name":"_xsrf"}).get('value')
    return value

#获取当时的验证码链接
def get_captcha():
    timestamp = str(time.time()*1000).split(".")[0]
    url = "https://www.zhihu.com/captcha.gif?r=%s&amp;type=login&amp;lang=cn" % timestamp
    print(url)
    req = session.get(url,headers=headers)
    with open("img1.png",'wb') as f:
        f.write(req.content)

#采集到验证码的坐标，通过查看倒立汉字的位置，模拟点击的点
def get_code():
    get_captcha()
    print("输入倒立汉字的位置，用逗号隔开")
    a = input("input:")
    indexs = a.split(",")
    data=[[16.4,26.9],[33.4,26.9],[60.4,21.9],[84.4,24.9],[108.4,24.9],[130.4,24.9],[156.4,24.9]]
    input_points = []
    for idx in indexs:
        input_points.append(data[int(idx)-1])
    dict = {
        "img_size": [200, 44],
        "input_points": input_points
    }
    return dict

#模拟登录
def login():
    url = "https://www.zhihu.com/login/phone_num"
    data={
        "_xsrf":get_xsrf(),
        "phone_num":'18200590129',
        "password":'chenyuejun900129',
        'captcha':get_code()
    }
    response = session.post(url, data=data,headers=headers)
    print(response)
    print(response.text)
    # login_code = response.json()
    # print(login_code['msg'])
    # response = session.get("https://www.zhihu.com/settings/profile",headers=headers)
    # #将cookies->dict->json存放在txt|之后再json->dict直接使用
    # with open("cookies.txt",'w') as f:
    #     json.dump(session.cookies.get_dict(),f)
    # with open("login.html","wb") as f:
    #     f.write(response.content)

login()