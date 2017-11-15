#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : customUserAgent.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/15
# @Desc  :


from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from fake_useragent import UserAgent

class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        '''
                定义下载中间件，
                必须要写这个函数，
                这是scrapy数据流转的一个环节
                具体可以看文档:
                http://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/downloader-middleware.html
                '''
        # ua = random.choice(agents)
        ua = UserAgent()
        request.headers.setdefault('User-Agent',ua.random)

