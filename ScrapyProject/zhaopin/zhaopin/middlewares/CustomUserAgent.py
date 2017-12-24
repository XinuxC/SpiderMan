#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : CustomUserAgent.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/12/23
# @Desc  :


from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from fake_useragent import UserAgent  # https://pypi.python.org/pypi/fake-useragent

class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        '''
                定义下载中间件，
                必须要写这个函数，
                这是scrapy数据流转的一个环节
                具体可以看文档:
                http://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/downloader-middleware.html
                '''
        ua = UserAgent()
        request.headers.setdefault('User-Agent',ua.random)
