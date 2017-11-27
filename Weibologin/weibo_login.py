#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : weibo_login.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/9
# @Desc  :
import json
import re
import urllib
import binascii
import rsa
import requests
import base64



'https://github.com/xchaoinfo/fuck-login'

headers = {
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    # 'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
}



def user_login(username,password):
    session = requests.Session()

    prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=eWFvX2ppbmdfMDEyOSU0MGhvdG1haWwuY29t&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1510281990690'
    push_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'

    r = session.get(prelogin_url)  # 请求prelogin_url 得到post_data需要的数据
    json_data = re.findall(r'({.*?})',r.text)[0]  # 提取出字典类型的str
    data = json.loads(json_data)  # 将str转成dict类型数据

    # 添加post_data数据
    servertime = data['servertime']
    nonce = data['nonce']
    pubkey = data['pubkey']
    rsakv = data['rsakv']

    # 得到su
    username = urllib.parse.quote(username)
    su = base64.b64encode(username.encode(encoding='utf-8'))
    # 得到sp
    rsaPublickey = int(pubkey,16)
    key = rsa.PublicKey(rsaPublickey,65537)  #
    message = str(servertime) +'\t' + str(nonce) + '\n' +str(password)
    sp = binascii.b2a_hex(rsa.encrypt(message.encode(encoding='utf-8'),key))

    #组装post_data
    post_data = {
        'entry' : 'weibo',
        'gateway' : '1',
        'from':'',
        'savestate' :'7',
        'useticket':'1',
        'ssosimplelogin':'1',
        'vsnf':'1',
        'vsnval':'',
        'su':su,
        'service':'miniblog',
        'servertime':servertime,
        'nonce':nonce,
        'pwencode':'rsa2',
        'rsakv':rsakv,
        'sp':sp,
        'encoding':'UTF-8',
        'url':'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype':'META'
        }
    # 向登录url post数据
    resp = session.post(push_url,post_data)
    login_url = re.findall(r'(https://.*?)"',resp.text)  # 找出结果中的登录url
    # print(login_url)

    response = session.get(login_url[0])  # 请求上面找到的url
    redirect_url = re.findall(r'(https://weibo.com/ajaxlogin.php.*?)\'',response.text)  # 得到跳转url
    # 请求跳转页面 找出uid
    uid_resp = session.get(redirect_url[0])
    uid = re.findall('"uniqueid":"(\d+)"',uid_resp.text)[0]
    # print(uid)
    url = "https://weibo.com/u/" + uid
    # 登录成功
    r = session.get(url)
    print(r.text)


if __name__ == '__main__':
    username = input("用户名:")
    password = input("密码:")
    user_login(username=username,password=password)