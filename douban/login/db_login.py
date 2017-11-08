#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : db_login.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/8
# @Desc  :
import os
import requests
# from HTMLParser import HTMLParser
import re
from bs4 import BeautifulSoup
from PIL import Image


headers ={
        'Host': 'accounts.douban.com',
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        # 'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        'Referer': 'https://www.douban.com/',
    }

session = requests.Session()

url = 'https://accounts.douban.com/login'
# url = 'https://www.douban.com/accounts/login'
movie_url ='https://movie.douban.com/'



def save(html):
    with open('movie.html','w',encoding='utf-8') as f :
        f.write(html)

def login(account,password):
    postdata = {

        'redir' : 'https://www.douban.com',
        'form_email': account,
        'form_password': password,
        # 'login' : u'登录'
    }
    r = session.post(url,data=postdata,headers=headers)
    bsObj = BeautifulSoup(r.text, "html.parser")
    captcha_image_tag = bsObj.select('.captcha_image')
    captcha_url = captcha_image_tag[0]['src']
    # print(captcha_url)
    image = requests.get(captcha_url)
    with open('captcha.jpg', 'wb') as f:
        f.write(image.content)
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input('请输入验证码:')
    captcha_id = re.findall(r'<input type="hidden" name="captcha-id" value="(.*?)"/>', r.text)
    postdata['captcha-solution'] = captcha
    postdata['captcha-id'] = captcha_id
    r = session.post(url=url,data=postdata,headers=headers)
    movie = session.get(movie_url)
    # print(r.text)
    save(movie.text)


if __name__ == '__main__':
    account = input("输入用户名:")
    password = input("输入密码:")
    login(account, password)
