#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/12/15
# @Desc  :

from scrapy.cmdline import  execute
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','zhihuspider'])






