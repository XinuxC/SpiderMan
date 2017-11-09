#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/11/9
# @Desc  :
import json

import requests
from bs4 import BeautifulSoup
from lxml import etree
import time


headers = {
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    # 'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Cookie' : 'aliyungf_tc=AQAAAFNMLEqvWwgA2pPq25MOdJIV2w3n; q_c1=a02bfc29e6a84de6b41b4efcb9ebbc5a|1510197047000|1510197047000; _xsrf=1c108a6651084829a2bf637094b9a0e9; d_c0="AFDCBTjEpwyPTqGfUnWevf_hBHokIIjmgEc=|1510197048"; _zap=8b61f6bc-6143-41b7-b0c3-80554bdb8563; z_c0=Mi4xSnRWX0FnQUFBQUFBVU1JRk9NU25EQmNBQUFCaEFsVk5Jelh4V2dBcVd4dzhxdlVWN1dVbWY0ZW0wR1ctODF0ZzB3|1510205219|e0e5acf9df3a3214d43f9a73910d776b2e7ed1e7; r_cap_id="MzFiMzI1NTZkMDkzNDMxYWEyMmNkNjFiMjkxNzIzMmY=|1510205218|456979acc41881300fbbc86c287487373fe18a62"; cap_id="ZWFlZjg1Y2Y2MDkwNDgxZmE2Yzg3MDg4Yzk4YzBjMmE=|1510205218|b3dc345bda0ba166f850d4bcfc059c82bf42650d"; __utma=155987696.615021754.1510205763.1510205763.1510205763.1; __utmc=155987696; __utmz=155987696.1510205763.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _xsrf=1c108a6651084829a2bf637094b9a0e9'
}

session = requests.Session()
for page in range(0,260,20):
    # url = 'https://www.zhihu.com/people/XinuxC/following?page=' + str(page + 1)
    url = 'https://www.zhihu.com/api/v4/members/MagicNumber/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&' \
          'offset={}&limit=20'.format(page)
    # print(url)
    r = session.get(url,headers=headers)
    r.encoding = 'utf-8'
    followees = json.loads(r.text)
    print(type(followees))  #
    print(type(followees['paging']))
    print(type(followees['data']))

    for i in followees['data']:
        print('用户:%s\tHeadline:%s' %(i['name'], i['headline']))
    time.sleep(2)


