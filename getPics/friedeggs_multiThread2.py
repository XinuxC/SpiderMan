#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : friedeggs_multiThread2.py
# @Author: ChENMo
# @Contact : pishit2009@gmail.com 
# @Date  : 2017/9/26
# @Desc  : 每个线程跑一个页面,如果页面太多，可以用队列 queue 来控制线程数量


import  requests,re,os,time,threading

# def getPics(page):
#     url='http://jandan.net/ooxx/page-%s' % page
#     dirpath=r'D:\meizitu'
#
#     if not os.path.isdir(dirpath):
#         os.mkdir(dirpath)
#
#     myHeaders={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
#             'Referer':'http://jandan.net/ooxx',
#             'Host':'jandan.net'
#         }
#     req=requests.get(url,headers=myHeaders)
#
#     # string='ws4.sinaimg.cn/large/7b386511gy1fjw6decinbj20fy0igaoi.jpg'
#     s=req.text
#     pattern=r'w.*?.sinaimg.cn/large/.*?.jpg|w.*?.sinaimg.cn/large/.*?.gif'
#     results=re.findall(pattern,s)
#     # print(result)
#
#     for jpgs in results:
#         startTime = time.time()
#         jpg=''.join(jpgs.split('/')[2])
#         print("Downloading:", jpg)
#         urls = 'http://' + jpgs
#         res=requests.get(urls)
#         filename=os.path.join(dirpath,jpg)
#         # print(filename)
#         with open(filename,'wb') as f :
#             f.write(res.content)
#         print('...done')
#         print(time.time()-startTime)
#
# if __name__ == '__main__' :
#     initPage = input('输入起始页:')
#     endPage = input('输入终止页:')
#     for page in range(int(initPage),int(endPage)+1):
#         threading._start_new_thread(getPics,(page,))
#
#     input('按回车退出...')


# def getPics():
#     initPage = input('输入起始页:')
#     endPage = input('输入终止页:')
#     for page in range(int(initPage),int(endPage)+1):
#         print('thread %s is running...(%s)' % (threading.current_thread().name, os.getpid()))
#         url='http://jandan.net/ooxx/page-%s' % page
#         dirpath=r'D:\meizitu'
#
#         if not os.path.isdir(dirpath):
#             os.mkdir(dirpath)
#
#         myHeaders={
#                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
#                 'Referer':'http://jandan.net/ooxx',
#                 'Host':'jandan.net'
#             }
#         req=requests.get(url,headers=myHeaders)
#
#         # string='ws4.sinaimg.cn/large/7b386511gy1fjw6decinbj20fy0igaoi.jpg'
#         s=req.text
#         pattern=r'w.*?.sinaimg.cn/large/.*?.jpg|w.*?.sinaimg.cn/large/.*?.gif'
#         results=re.findall(pattern,s)
#         # print(result)
#
#         for jpgs in results:
#             startTime = time.time()
#             jpg=''.join(jpgs.split('/')[2])
#             print("Downloading:", jpg)
#             urls = 'http://' + jpgs
#             res=requests.get(urls)
#             filename=os.path.join(dirpath,jpg)
#             # print(filename)
#             with open(filename,'wb') as f :
#                 f.write(res.content)
#             print('...done')
#             print(time.time()-startTime)
#         print('thread %s ended.' % threading.current_thread().name)
#
# if __name__ == '__main__' :
#     print('thread %s is running...(%s)' % (threading.current_thread().name, os.getpid()))
#     t1 = threading.Thread(target=getPics,name='DownloadPics')
#     t1.start()
#     t1.join()
#     print('thread %s ended.' % threading.current_thread().name)
#     input('按回车退出...')


def getPics(page):
    url='http://jandan.net/ooxx/page-%s' % page
    dirpath=r'D:\meizitu'

    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

    myHeaders={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer':'http://jandan.net/ooxx',
                'Host':'jandan.net'
            }
    req=requests.get(url,headers=myHeaders)

    # string='ws4.sinaimg.cn/large/7b386511gy1fjw6decinbj20fy0igaoi.jpg'
    s=req.text
    pattern=r'w.*?.sinaimg.cn/large/.*?.jpg|w.*?.sinaimg.cn/large/.*?.gif'
    results=re.findall(pattern,s)
    # print(result)

    for jpgs in results:
        startTime = time.time()
        jpg=''.join(jpgs.split('/')[2])
        print("Downloading:", jpg)
        urls = 'http://' + jpgs
        res=requests.get(urls)
        filename=os.path.join(dirpath,jpg)
        # print(filename)
        with open(filename,'wb') as f :
            f.write(res.content)
        print('...done')
        print(time.time()-startTime)


if __name__ == '__main__' :
    initPage = input('输入起始页:')
    endPage = input('输入终止页:')
    for page in range(int(initPage), int(endPage) + 1):
        t1 = threading.Thread(target=getPics,args=(page,),name='DownloadPics')
        t1.start()
        t1.join()

    input('按回车退出...')