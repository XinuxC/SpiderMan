#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : spider.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/24
# @Desc  : 今日头条街拍图片
import json
import re
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)

    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        print("请求索引页出错")
        return None

#解析请求的数据,返回articleURL列表
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        print("请求详情页出错",url)
        return None

def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    image_pattern = re.compile(r'gallery:(.*?);',re.S)
    result = re.search(image_pattern,html)
    if result:
        data = json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
                'title':title,
                'url':url,
                'images':images
            }

def main():
    html = get_page_index(0,'街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            print(result)

# if __name__ == '__main__':
#     main()

html_init = get_page_index(0,'街拍')
# print(html_init)
for url in parse_page_index(html_init):
    html = get_page_detail(url)
    # print(html)
    if html :
        soup = BeautifulSoup(html,'lxml')
        title = soup.select('title')[0].get_text()
        # print(title)
        image_pattern = re.compile(r'gallery:(.*?)siblingList',re.S)
        result = re.search(image_pattern,html)
        if result:
            s = result.group(1).rstrip(',')
            print(s)
            # data = json.loads(result.group(1)[:-1])
            # if data and 'sub_images' in data.keys():
            #     sub_images = data.get('sub_images')
            #     images = [item.get('url') for item in sub_images]
            #     print(images)