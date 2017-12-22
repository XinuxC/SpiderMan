#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : utils.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/12/22
# @Desc  :

import re
import hashlib


def addr_strip(value):
    addr_list = [item for item in value.strip() if value.strip()!= "查看地图"]
    return addr_list

def remove_backlash(value):
    return value.strip('/')

def url_md5(value):
    if isinstance(value,str):  # python3中没有Unicode关键词了,str就是Unicode的类型了
        url = value.encode('utf-8')
        m = hashlib.md5()
        m.update(url)  # Unicode会报错,encode成utf8
        return m.hexdigest()  # 抽取摘要

def get_time(value):
    p = r'(.*?)  发布于拉勾网'
    result = re.findall(p,value)
    return result