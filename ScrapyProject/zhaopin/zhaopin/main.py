#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/12/21
# @Desc  :

from scrapy.cmdline import execute
import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','lagou'])
