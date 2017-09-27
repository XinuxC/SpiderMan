#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : friedeggs_multiThread.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/26
# @Desc  : 对单个页面的多张图片使用多线程,但是这样做的话，线程间的切换开销太大，不仅没有速度的提升，反而降低了程序运行的速度

import  requests,re,os,time,threading

print('图片在D:\meizitu')
page = input('请输入页码:')
url = 'http://jandan.net/ooxx/page-%s' % page  #  获取用户输入网页url
dirpath = r'D:\meizitu'  #  图片存储位置

if not os.path.isdir(dirpath):  #  检查路径是否存在,没有就创建
    os.mkdir(dirpath)

myHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'http://jandan.net/ooxx',
        'Host': 'jandan.net'
    }
req = requests.get(url, headers=myHeaders)

# string='ws4.sinaimg.cn/large/7b386511gy1fjw6decinbj20fy0igaoi.jpg'  #  页面中关于图片或gif的路径格式,根据此来写正则
s = req.text  #  获取网页内容以便获取图片地址
pattern = r'w.*?.sinaimg.cn/large/.*?.jpg|w.*?.sinaimg.cn/large/.*?.gif'  #  正则表达匹配图片路径
results = re.findall(pattern, s)  #  找出所有图片地址

def savaPics(jpgsName):
    startTime = time.time()
    jpg=''.join(jpgsName.split('/')[2])
    print("Downloading:", jpg)  #  输出打印图片名称
    picUrls = 'http://' + jpgsName  #  拼接处图片下载url
    res=requests.get(picUrls)  #  获取图片
    filename=os.path.join(dirpath,jpg)  #  图片完整路径加图片名
    with open(filename,'wb') as f :  #  获取的图片存入文件夹
        f.write(res.content)
    print(jpg,'...done')
    print('timecost:',time.time()-startTime)


if __name__ == '__main__' :
    for jpgsName in results:
        threading._start_new_thread(savaPics,(jpgsName,))
    input('press Enter to exit...')
