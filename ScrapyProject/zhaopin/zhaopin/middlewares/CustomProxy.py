#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : CustomProxy.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/12/24
# @Desc  :

from .getproxies import GetProxyIP

class RandomProxy(object):
    def process_request(self,request,spider):
        gp = GetProxyIP()
        proxy = gp._get_random_proxy()
        request.meta['proxy'] = proxy
