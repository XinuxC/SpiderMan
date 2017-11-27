#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : ComicSpider.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/27
# @Desc  :

import os
import re
import time

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def SavePic(filename, url):
    '''
    通过requests库
    将抓取到的图片保存到本地
    '''
    content = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(content)

def parse_chapter(url,header):
    r = requests.get(url,header)
    bsObj = BeautifulSoup(r.text,"html.parser")
    name = bsObj.title.string.split(',')[0]
    mkdir(name)
    link_tag = bsObj.find_all("div",{"class":"comic_Serial_list"})
    for i in range(len(link_tag)):
        pattern = re.compile(r'<a href="(.*?)" target="_blank">')
        hrefs = pattern.findall(str(link_tag[i]))
        # print(hrefs)
        links = []
        for href in hrefs:
            links.append(urljoin(url,href))
        # print(links)

    Comics = dict(name=name,urls=links)
    return Comics



def download_chapter(Comics):
    chapter_urls = Comics['urls']
    basedir = Comics['name']
    browser = webdriver.PhantomJS(r'C:\Users\30594\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    # browser = webdriver.Chrome(r'C:\Users\30594\chromedriver\chromedriver.exe')
    for chapter in chapter_urls:
        browser.get(chapter)
        browser.implicitly_wait(3)

        #创建章节目录
        dirname = basedir + os.sep + browser.title.split('-')[1]
        mkdir(dirname)

        pageNum = len(browser.find_elements_by_tag_name('option'))

        #下一页按钮
        nextPage = browser.find_element_by_xpath('/html/body/div[3]/div[1]/a[3]')

        for i in range(pageNum):
            pic_url = browser.find_element_by_id('curPic').get_attribute('src')
            print(pic_url)
            filename = dirname + os.sep + str(i) + '.jpg'
            SavePic(filename,pic_url)
            # time.sleep(2)
            nextPage.click()
        print('当前章节下载完毕')

    browser.quit()
    print('所有章节下载完毕')



def main():
    header = {
        'Host': 'Host:manhua.sfacg.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    url = 'http://manhua.sfacg.com/mh/BiaoRen/'
    Cosmic = parse_chapter(url,header)
    download_chapter(Cosmic)

if __name__ == '__main__':
    main()
