#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : studyrequests.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/28
# @Desc  :  requests学习
import json

import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
#基本POST请求,对于 POST 请求来说，我们一般需要为它增加一些参数。那么最基本的传参方法可以利用 data 这个参数。
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

#会话对象:我们需要保持一个持久的会话怎么办
url='https://www.zhihu.com'
s = requests.Session()
r = s.get(url)
print(type(r))
print(r.status_code)
print(r.cookies)
# print(r.text)

#SSL证书验证 verify=False/True
r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print(r.cookies)

#代理 如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print(r.text)

s = requests.Session()
r = s.get('https://github.com/timeline.json')
print(type(r.text))

# print(r.cookies)
# Requests 中也有一个内置的 JSON 解码器，助你处理 JSON 数据：
print(type(r.json()))
#需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。
# 有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回。
# 要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。
# print(r.status_code)
# 内置模块json同样可以处理json数据
# data = json.loads(r.text)
# print(data == r.json())

r = requests.get('https://github.com/timeline.json')
# print(r.encoding)

#二进制响应内容
print(r.content)
#Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据。
#例如，以请求返回的二进制数据创建一张图片，你可以使用如下代码：
from PIL import Image
from io import BytesIO
i = Image.open(BytesIO(r.content))


with open('test.txt', 'wb') as fd:
    for chunk in r.iter_lines():
        fd.write(chunk)

for chunk in r.iter_lines():
        print(chunk)


#POST一个多部分编码(Multipart-Encoded)的文件
url = 'http://httpbin.org/post'
files = {'file': open('homecoming.py', 'rb')}
#也可以发送作为文件来接收的字符串
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url,files=files)
# print(r.text)


#Cookie
#如果某个响应中包含一些 cookie，你可以快速访问它们：
url = 'https://zhihu.com'
r = requests.get(url)
print(r.cookies)
#要想发送你的cookies到服务器，可以使用 cookies 参数：
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

#Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但界面更为完整，适合跨域名跨路径使用。
# 你还可以把 Cookie Jar 传到 Requests 中：
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)

#重定向与请求历史
#默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
#可以使用响应对象的 history 方法来追踪重定向。
#Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。
#如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理：
r = requests.get('http://github.com',allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.history)
#如果你使用了 HEAD，你也可以启用重定向：
r = requests.head('http://github.com', allow_redirects=True)


