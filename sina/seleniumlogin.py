#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : seleniumlogin.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/21
# @Desc  :

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

broswer = webdriver.Chrome(r'C:\Users\XinuxC\chromedriver_win32\chromedriver.exe')
wait = WebDriverWait(broswer,30)
def login():
    username = input("输入用户名:")
    passwd = input("输入密码:")
    print("登录中...")
    try:
        broswer.get('https://weibo.com/')
        input_username  = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#loginname")))
        input_pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#pl_login_form > div > div:nth-child(3) > div.info_list.password > div > input")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#pl_login_form > div > div:nth-child(3) > div.info_list.login_btn > a > span")))
        input_username.clear()
        input_username.send_keys(username)
        input_pwd.clear()
        input_pwd.send_keys(passwd)
        submit.click()
        # mainpage = wait.until(EC.presence_of_all_elements_located())
    except TimeoutError:
        return login()




if __name__ == '__main__':
    login()

