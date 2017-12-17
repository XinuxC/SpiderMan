#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zhihulogin.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/29
# @Desc  :




import requests
try:
    import cookielib
except:
    import http.cookiejar
import re
import time
import os
try:
    from PIL import Image
except:
    pass
import json

from lxml import etree


#根据网站报头信息设置headers
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
    'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',

}

session = requests.Session()
# # 从txt文件中获取cookies,json->dict存入session.cookies
# with open("cookies.txt",'r') as f:
#     cookies = json.load(f)
# session.cookies.update(cookies)


#获取_xsrf
def getXSRF():
    index_url = 'https://www.zhihu.com'
    r = session.get(url=index_url,headers=headers)
    s = str(r.cookies)
    pattern = r'_xsrf=(.*?) for'
    xsrf = re.findall(pattern, s, re.S | re.I)
    _xsrf = xsrf[0]
    return _xsrf

def get_captcha():
    t = str(int(time.time() * 1000))
    # 手机登录验证码地址
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    image = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(image.content)
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input('请输入验证码:')
    return captcha

def login(account,password):
    if re.match(r'1\d{10}$',account):
        print("手机号登录\n")
        url = 'https://www.zhihu.com/login/phone_num'
        # 分析构造post数据
        postDict = {
        '_xsrf': getXSRF(),
        'phone_num': account,
        'password': password,
        'captcha': get_captcha()
        }
    else:
        if '@' in account :
            print("邮箱登录\n")
        else:
            print("输入账号有问题,重新登录")
            return 0
        url = "https://www.zhihu.com/login/email"
        postDict = {
            '_xsrf': getXSRF(),
            'email': account,
            'password': password,
            'captcha': get_captcha()
        }
    r = session.post(url=url,data=postDict,headers=headers)
    # print(r.text)
    with open("cookies.txt", 'w') as f:
        json.dump(session.cookies.get_dict(), f)



def  isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    r =  session.get(url,headers=headers,allow_redirects=False)
    if r.status_code == 200 :
        return  True
    else:
        return False

def get_following():
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        # 'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',

    }

    followees_list=[]
    for page in range(0, 60, 20):
        url = 'https://www.zhihu.com/api/v4/members/XinuxC/followees?' \
              'include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed' \
              '%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&' \
                  'offset={}&limit=20'.format(page)
        r = session.get(url, headers=headers)
        r.encoding = 'utf-8'
        followees = json.loads(r.text)
        followees_list+=followees['data']
        time.sleep(2)
    # return followees_list
        for i in followees_list:
            print('用户:%s\tHeadline:%s' % (i['name'], i['headline']))





if __name__ == '__main__':
    if isLogin():
        print("已登录")
        get_following()

    else:
        account = input("请输入用户名:")
        password = input("请输入密码:")
        login(account,password)
        get_following()


