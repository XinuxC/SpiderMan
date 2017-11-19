#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : maoyanmovie.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/19
# @Desc  :
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pymysql

# browser = webdriver.Chrome(r'C:\Users\30594\chromedriver\chromedriver.exe')
browser = webdriver.PhantomJS(r'C:\Users\30594\phantomjs-2.1.1-windows\bin\phantomjs.exe')
wait = WebDriverWait(browser,30)
browser.set_window_size(1400,900)  #设置窗口大小,默认比较小,影响模拟浏览器操作
def search():
    print('searching')
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button"))
        )
        input.send_keys("美食")
        submit.click()
        total_pages = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))
        get_products()
        return total_pages.text
    except TimeoutError:
        return search()

def next_page(page_number):
    print('翻到:',page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page_number)
            )
        )
        get_products()
    except TimeoutError:
        return next_page(page_number)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()  # items()得到所有选择的内容
    # print(items)
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deals':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        save_to_mysql(product)
        # print(product)

conn = pymysql.connect(
            host='219.234.147.218',
            port=23306,
            user='root',
            passwd='yaojing0129',
            db='scrapyDB',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

def save_to_mysql(product):
    title = product['title']
    price= product['price']
    image = product['image']
    deals = product['deals']
    shop = product['shop']
    location = product['location']

    with conn.cursor() as cur:
            sql = 'insert into taobao(title,price,image,deals,shop,location) ' \
                  'values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (title, price, image, deals, shop, location)
            if cur.execute(sql):
                print('保存数据成功')
            else:
                print('保存数据失败')
    conn.commit()


def main():
	try:
	    total_pages = search()
	    pages = int(re.compile('(\d+)').search(total_pages).group(1))
	    print(pages)
	    for page in range(2,pages+1):
	        next_page(page)
	except Exception:
		print("出错啦")
	finally:
		browser.close()
        conn.close()

if __name__ == '__main__':
    main()
