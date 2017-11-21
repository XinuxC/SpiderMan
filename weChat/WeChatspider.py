#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : WeChatspider.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/20
# @Desc  :
import os

import re
import itchat

#login
itchat.login()

#send msg
# friends = itchat.get_friends(update=True)
# itchat.send_image('D:\python\weChat\signature.jpg')

#get all friends(including me) to caculate male/female percentage
friends = itchat.get_friends(update=True)
# for friend in friends:
#     print(friend)

male = female = others = 0
total = len(friends)
for i in friends[:]:
    sex = i['Sex']
    if sex == 1:
        male +=1
    elif sex == 2:
        female += 1
    else:
        others +=1
print('男性 %.2f%%' % (float(male)/total*100))
print('女性 %.2f%%' % (float(female)/total*100))
print('其他 %.2f%%' % (float(others)/total*100))

#获取好友个性签名 做成词云
signatures = []
for i in friends:
    # signature = i['Signature']
    signature= i['Signature'].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d.+")
    signature = rep.sub("",signature)
    signatures.append(signature)
# print(signature)
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
from    collections import Counter
#拼接字符串
text = ''.join(signatures)
#jieba分词
# wordlist = jieba.cut(text,cut_all=True)
wordlist = jieba.cut(text)
wl_space_split = " ".join(wordlist)

#wordcloud词云
background = np.array(Image.open(os.path.join('D:\Git\SpiderMan\weChat','20171120222644.jpg')))
my_wordCloud = WordCloud(background_color="white",
                         max_words = 5000,  # 词云显示最大词数
                         mask = background,  # 设置背景
                         max_font_size=100,  # 字体最大值
                         random_state=42,
                         font_path='D:\python\weChat\STXINGKA.TTF',  # 设置字体
                         width=1000,
                         height=860,  # 设置图片默认大小
                         margin=2).generate(wl_space_split)
image_color = ImageColorGenerator(background)
plt.imshow(my_wordCloud.recolor(color_func=image_color))
plt.figure()
plt.imshow(my_wordCloud)
plt.axis("off")
plt.show()
my_wordCloud.to_file('sgn.jpg')



#conver to chart
# import echarts
# chart = echarts.Echart(u'%s的微信好友性别比例'%(friends[0]['NickName']),'from WeChat')
# chart.use(echarts.Pie('WeChat',
#               [{'value':male,'name':u'男性 %.2f%%' % (float(male)/total*100)},
#                {'value':female,'name':u'女性 %.2f%%' % (float(female)/total*100)},
#                {'others':others,'name':u'人妖 %.2f%%' % (float(others)/total*100)}
#               ],
#               radius = ['50%','70%']
#               ))
# chart.use(echarts.Legend(['male','female','others']))
# del chart.json['xAxis']
# del chart.json['yAxis']
# chart.plot()  #Mac os下可用



