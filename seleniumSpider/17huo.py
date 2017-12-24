#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lesson3.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com
# @Date  : 2017/11/7
# @Desc  : Selenium 简介和实战 使用css_selector


from selenium import webdriver
import time

# browser = webdriver.Chrome()
# browser = webdriver.Chrome(r'C:\Users\XinuxC\chromedriver_win32\chromedriver.exe')
browser = webdriver.Chrome(r'C:\Users\30594\chromedriver\chromedriver.exe')
browser.set_page_load_timeout(30)
browser.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')
# print(page_info.text)
pages = int((page_info.text.split('，')[0]).split(' ')[1])
for page in range(pages):
    if page > 2:
        break
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')

    print('%d页有%d件商品' % ((page + 1), len(goods)))
    for good in goods:
        try:
            # body > div.wrap > div:nth-child(2) > div.p_main > ul > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)
            # body > div.wrap > div:nth-child(2) > div.p_main > ul > li:nth-child(2) > a:nth-child(1) > p:nth-child(2)
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            #body > div.wrap > div:nth-child(2) > div.p_main > ul > li:nth-child(1) > div > a > span
            #body > div.wrap > div:nth-child(2) > div.p_main > ul > li:nth-child(2) > div > a > span
            price = good.find_element_by_css_selector('div > a > span').text
            print(title, price)
        except:
            print(good.text)

browser.close()
