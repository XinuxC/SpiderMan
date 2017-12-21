#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : zheyelogin.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/12/20
# @Desc  :
import re

import requests
import time

from zheye import zheye


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    # 'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',

}


session = requests.session()

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
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login&lang=cn"  # 倒立验证码图片地址
    image = session.get(captcha_url, headers=headers)
    with open('captcha.gif', 'wb') as f:
        f.write(image.content)

    z = zheye()
    positions = z.Recognize('captcha.gif')

    return positions

def login():
    login_url = 'https://www.zhihu.com/login/phone_num'
    positions = get_captcha()
    """
    captcha:{'img_size:[200,44],'input_points':[[63.375,23],[107.375,24]]    """

    post_data = {
        '_xsrf': getXSRF(),
        'phone_num': '18200590129',
        'password': 'chenyuejun900129',
        'captcha_type':'cn',
        'captcha': '{"img_size":[200,44],"input_points":[[%.3f,%.2f],[%.3f,%.2f]]}' % (positions[0][1] /2,positions[0][0] /2 ,positions[1][1] /2,positions[1][0] /2)
    }
    r = session.post(login_url,headers=headers,data=post_data)
    print(r.text)


def main():
    login()


if __name__ == '__main__':
    main()