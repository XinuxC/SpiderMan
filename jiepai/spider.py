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
    image_pattern = re.compile(r'gallery:(.*?)\n', re.S)  # 详情页里图片url都在返回的gallery里,在此提取
    result = re.search(image_pattern,html)
    if result:
        data = json.loads(result.group(1).rstrip(','))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
                'title':title,
                'url':url,
                'images':images
            }

# 保存图片
def save_iamge(urls):
    for  url in urls:
        r = requests.get(url)
        imageName = url.split('/')[-1]+'.jpg'
        print('downloading ',imageName)
        with open(imageName,'wb') as f :
            f.write(r.content)
        print('...done')


def main():
    html = get_page_index(0,'街拍')  # 得到索引页的返回html
    for url in parse_page_index(html):  # 解析索引页 得到返回的文章url列表
        html = get_page_detail(url)  # 得到返回的html(跟get_page_index几乎一样,只是函数里url动态传递进去)
        if html:
            result = parse_page_detail(html,url)  # 得到详情页r.text对象后解析内容,得到json对象 打印输出
            if result:
                images_url = result['images']
                save_iamge(images_url)

if __name__ == '__main__':
    main()





