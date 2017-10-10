#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : SeniorRequests.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/10
# @Desc  :


import requests

s = requests.Session()
# print(type(r))
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)