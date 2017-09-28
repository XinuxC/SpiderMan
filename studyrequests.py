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
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)
#
# #会话对象:我们需要保持一个持久的会话怎么办
# url='https://www.zhihu.com'
# s = requests.Session()
# r = s.get(url)
# print(type(r))
# print(r.status_code)
# print(r.cookies)
# # print(r.text)
#
# #SSL证书验证 verify=False/True
# r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
# print(r.cookies)
#
# #代理 如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
# proxies = {
#   "https": "http://41.118.132.69:4433"
# }
# r = requests.post("http://httpbin.org/post", proxies=proxies)
# print(r.text)

s = requests.Session()
r = s.get('https://github.com/timeline.json')
print(r.text)
print(r.content)
print(r.cookies)


r=requests.get('https://github.com/timeline.json')
print(r.text)
# Requests 中也有一个内置的 JSON 解码器，助你处理 JSON 数据：
print(r.json())
#需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。
# 有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回。
# 要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。
print(r.status_code)
# 内置模块json同样可以处理json数据
# data = json.loads(r.text)
# print(data == r.json())

#http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
#http://www.cnblogs.com/puyangsky/p/5326384.html
