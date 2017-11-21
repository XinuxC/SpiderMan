#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lesson3.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/7
# @Desc  : Selenium 简介和实战

import time
from selenium import webdriver



#指定路径,解决selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH错误
browser = webdriver.Chrome(r'C:\Users\XinuxC\chromedriver_win32\chromedriver.exe')
# browser = webdriver.Chrome()
#设置超时时间
browser.set_page_load_timeout(30)

# browser.get('http://hz.17zwd.com/sks.htm?so=%E5%A4%A7%E8%A1%A3')
# #页数的css选择器格式:#mainsrp-pager > div > div > div > div.total,只有一个页数元素,顾使用find_element
# page_info = browser.find_element_by_css_selector('#pages__pager_2 > div > span:nth-child(8)')
# #也是格式是:共 100 页 ,拆分得到100
# # print(page_info.text.split()[0][1:])
# pages = int(page_info.text.split()[0][1:])
# print('商品%d页' % pages)
#
# for page in range(pages):
#     if  page > 2:
#         break
#     print('第%d 页' % (page+1))
#     url = 'http://hz.17zwd.com/sks.htm?so=%E5%A4%A7%E8%A1%A3&page=' + str(page+1)
#     browser.get(url)
#     # browser.execute_script("window.scrollTo(0,document.body.scrollHeight);") #  如果是动态加载的 使用翻滚加载整个页面商品
#     # time.sleep(2)
#     # 商品的css_selector
#     # body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container > div > div:nth-child(1)
#     # body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container > div > div:nth-child(2)
#     goods = browser.find_element_by_css_selector('body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container').find_elements_by_css_selector('div.huohao-item')
#     # print(len(goods))
#
#     for good in goods :
#         # body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container > div > div:nth-child(3) > div:nth-child(3) > div > a
#         # body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container > div > div:nth-child(4) > div:nth-child(3) > div > a
#         title = good.find_element_by_css_selector('div:nth-child(3) > div > a').text
#
#         # body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container > div > div:nth-child(3) > div:nth-child(2) > div.row-price
#         # body > div > div.sks-clear-container.big-box > div > div.promote-market-goods-container > div.huohao-list-container > div > div:nth-child(3) > div:nth-child(2)
#         price = good.find_element_by_css_selector('div:nth-child(2) > div.row-price').text
#         print(title, price)



#淘宝爬取
browser.get('https://s.taobao.com/search?q=%E5%A4%A7%E8%A1%A3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171107&ie=utf8')
#页数的css选择器格式:#mainsrp-pager > div > div > div > div.total,只有一个页数元素,顾使用find_element
page_info = browser.find_element_by_css_selector('#mainsrp-pager > div > div > div > div.total')
#也是格式是:共 100 页 ,拆分得到100
pages = int(page_info.text.split(' ')[1])
print('商品共%d页' % pages)

for page in range(pages):
    if  page > 2:
        break
    print('第%d 页' % (page+1))
    url = 'https://s.taobao.com/search?q=%E5%A4%A7%E8%A1%A3&imgfile=&' \
          'js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171107&ie=utf8' \
          '&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=' + str(page+1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);") #  如果是动态加载的 使用翻滚加载整个页面商品
    time.sleep(2)
    # 商品的css_selector
    ##mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1)
    ##mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(2)
    goods = browser.find_element_by_css_selector('#mainsrp-itemlist > div > div').find_elements_by_css_selector('.item.J_MouserOnverReq')
    print(len(goods))

    for good in goods :
        # #mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(4) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-2.title
        # #mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(5) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-2.title
        title = good.find_element_by_css_selector('div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-2.title').text

        # #mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(5) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-1.g-clearfix > div.price.g_price.g_price-highlight
        # #mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(7) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-1.g-clearfix > div.price.g_price.g_price-highlight
        price = good.find_element_by_css_selector('div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-1.g-clearfix > div.price.g_price.g_price-highlight').text

        # #J_itemlistPersonality > div > div:nth-child(6) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a
        # #J_itemlistPersonality > div > div:nth-child(11) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a
        shop = good.find_element_by_css_selector('div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a').text

        addr = good.find_element_by_css_selector('div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a').get_attribute('href')

        # proper = good.find_element_by_css_selector('div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a').get_property('href')


        # #mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(3) > div.pic-box.J_MouseEneterLeave.J_PicBox > div > div.pic > a
        detail = good.find_element_by_css_selector('div.pic-box.J_MouseEneterLeave.J_PicBox > div > div.pic > a').get_property('href')
        print('店铺 {0} :{1}  的 {2} 价格是 {3},详情页:{4}'.format(shop,addr,title, price,detail))
