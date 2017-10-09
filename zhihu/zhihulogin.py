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
import os.path
try:
    from PIL import Image
except:
    pass
import  urllib

import urllib.request,gzip,re,http.cookiejar,urllib.parse
import sys
#解压缩函数
def ungzip(data):
    try:
        print("正在解压缩...")
        data = gzip.decompress(data)
        print("解压完毕...")
    except:
        print("未经压缩，无需解压...")
    return data

#构造文件头
def getOpener(header):
    #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cookieJar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookieJar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key,value in header.items():
        elem = (key,value)
        headers.append(elem)
    opener.addheaders = headers
    return opener

#获取_xsrf
def getXSRF():
    index_url = 'https://www.zhihu.com'
    r = requests.get(url=index_url,headers=headers)
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

#根据网站报头信息设置headers
headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Accept-Encoding': 'gzip, deflate,br',
    'Host': 'www.zhihu.com',
    'DNT':'1'
}

url = "https://www.zhihu.com/"
req=urllib.request.Request(url,headers=headers)
res=urllib.request.urlopen(req)

#读取知乎首页内容，获得_xsrf
data = res.read()
data = ungzip(data)
_xsrf = getXSRF()

opener = getOpener(headers)
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
url+='login/phone_num'
name='18200590129'
passwd='chenyuejun900129'

def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url='https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = requests.get(captcha_url,headers=headers)
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

#分析构造post数据
postDict={
    '_xsrf':_xsrf,
    'email':name,
    'password':passwd,
    'remember_me':'true'
}
postDict["captcha"] = get_captcha()

#给post数据编码
postData=urllib.parse.urlencode(postDict).encode()

#构造请求
res=opener.open(url,postData)
data = res.read()
#解压缩
data = ungzip(data)
print(data.decode())