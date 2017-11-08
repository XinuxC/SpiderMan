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

#根据网站报头信息设置headers
headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Accept-Encoding': 'gzip, deflate,br'
}

session = requests.Session()

#获取_xsrf
def getXSRF():
    index_url = 'https://www.zhihu.com'
    r = requests.get(url=index_url,headers=headers)
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

def login():
    # 读取知乎首页内容，获得_xsrf
    _xsrf = getXSRF()
    url = 'https://www.zhihu.com/signin?next='
    name = '18200590129'
    passwd = 'chenyuejun900129'
    # 分析构造post数据
    postDict = {
        '_xsrf': _xsrf,
        'email': name,
        'password': passwd,
        'remember_me': 'true'
    }
    headers['X-Xsrftoken'] = _xsrf
    headers['X-Requested-With'] = "XMLHttpRequest"
    r = session.post(url,headers=headers)
    pattern = r'https://www.zhihu.com/captcha.gif?r=.*?&type=login'
    image_url = re.findall(pattern,r.text)
    print(image_url)

    # with open('captcha.jpg','wb') as f :
    #     f.write(image.content)
    # try:
    #     im = Image.open('captcha.jpg')
    #     im.show()
    #     im.close()
    # except:
    #     print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    # captcha = input('请输入验证码:')
    # postDict['captcha'] = captcha
    # r = session.post(url=url,data=postDict,headers=headers)
    # print(r.text)

if __name__ == '__main__':
    login()

