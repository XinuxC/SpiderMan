#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zhihu.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/28
# @Desc  :


import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass


base_url = "https://www.zhihu.com"

# 构造 Request headers
base_headers = {
        'Host': 'www.zhihu.com',
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Referer': 'https://www.zhihu.com/',
    }
# # 使用登录cookie信息
session = requests.Session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ingore_discard=True)
except:
    print('Cookie 未能加载')

# 获取登录时需要用到的_xsrf
def getXSRF():
    index_url = 'https://www.zhihu.com'
    r = session.get(url=index_url,headers=base_headers)
    print(r.text)
    # get_xsrf
    s = str(r.cookies)
    # print(type(s))
    # print('cookie:', s)
    pattern = r'_xsrf=(.*?) for'
    xsrf = re.findall(pattern, s, re.S | re.I)
    # print(type(_xsrf))
    # print('_xsrf:', _xsrf)
    _xsrf = xsrf[0]
    return _xsrf

# # 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url='https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url,headers=base_headers)
    with open('captcha.jpg','wb') as f :
        f.write(r.content)
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input('请输入验证码:')
    return captcha


def  isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    status_code =  session.get(url,headers=base_headers,allow_redirects=False).status_code
    if status_code == 200 :
        return  True
    else:
        return False

def login(account,password):
    _xsrf = getXSRF()
    base_headers["X-Xsrftoken"] = _xsrf
    base_headers["X-Requested-With"] = "XMLHttpRequest"
    # 通过输入的用户名判断是否是手机号
    if re.match(r'1\d{10}$',account):
        print("手机号登录\n")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            '_xsrf': _xsrf,
            'password': password,
            'phone_num': account,
        }
    else:
        if '@' in account :
            print("邮箱登录\n")
        else:
            print("输入账号有问题,重新登录")
            return 0
        post_url = "https://www.zhihu.com/login/email"
        post_data = {
        '_xsrf': _xsrf,
        'password': password,
        'email': account,
        }
    # 不需要验证码直接登录成功
    login_page = session.post(post_url,post_data,base_headers)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        post_data["captcha"] = get_captcha()
        login_page = session.post(post_url,post_data,base_headers)
        login_code = login_page.json()
        print(login_code['msg'])
        # 保存 cookies 到文件，
        # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()

try:
    input = input()
except:
    pass

if __name__ == '__main__':
    if isLogin():
        print("已登录")
    else:
        account = input("输入用户名:")
        password = input("输入密码:")
        login(account,password)

