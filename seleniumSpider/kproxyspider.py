#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : kproxyspider.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/21
# @Desc  :

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.PhantomJS(r'C:\Users\XinuxC\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# wait = WebDriverWait(browser,10)


def  get_proxy():
    try:
        for i in range(1,3):
            browser.get('http://www.kuaidaili.com/free/inha/%s/' % i)
            browser.implicitly_wait(3)
            items = browser.find_elements_by_xpath('//*[@id="list"]/table/tbody/tr')
            proxy_list = []
            for item in items:
                ip = item.find_element_by_xpath('.//td[1]').text
                port = item.find_element_by_xpath('.//td[2]').text
                proxy_list.append(ip+':'+port)
            print(proxy_list)
            save_tofile(proxy_list)
    except Exception:
        print('出错啦')

def save_tofile(proxy_list):
    with open('proxt.txt','a') as f:
        for item in proxy_list:
            f.write(item + '\n')

if __name__ == '__main__':
    get_proxy()

