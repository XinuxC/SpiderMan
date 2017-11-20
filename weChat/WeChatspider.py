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
import numpy as np
from echarts import Echart, Legend, Pie
#login
itchat.login()

#send msg
itchat.send('hello')
# itchat.send_image('D:\python\weChat\signature.jpg')

#get all friends(including me) to caculate male/female percentage
friends = itchat.get_friends(update=True)

male = female = others = 0

for i in friends[:]:
    sex = i['Sex']
    if sex == 1:
        male +=1
    elif sex == 2:
        female += 1
    else:
        others +=1


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
import wordcloud
#拼接字符串
text = ''.join(signatures)
#jieba分词
wordlist = jieba.cut(text,cut_all=True)
wl_space_split = " ".join(wordlist)

#wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
modle = np.array(Image.open(os.path.join('D:\python\weChat','20171120223350.jpg')))
my_wordCloud = WordCloud(background_color="white",
                         max_words = 5000,
                         mask = modle,
                         max_font_size=100,
                         random_state=42,
                         font_path='D:\python\weChat\STXINGKA.TTF').generate(wl_space_split)
image_color = ImageColorGenerator(modle)
plt.imshow(my_wordCloud.recolor(color_func=image_color))
plt.imshow(my_wordCloud)
plt.axis("off")
plt.show()




#conver to chart
# chart = Echart(u'%s的微信好友性别比例'%(friends[0]['NickName']),'from WeChat')
# chart.use(Pie('WeChat',
#               [{'value':male,'name':u'男性 %.2f%%' % (float(male)/total*100)},
#                {'value':female,'name':u'女性 %.2f%%' % (float(female)/total*100)},
#                {'others':others,'name':u'人妖 %.2f%%' % (float(others)/total*100)}
#               ],
#               radius = ['50%','70%']
#               ))
# chart.use(Legend(['male','female','others']))
# del chart.json['xAxis']
# del chart.json['yAxis']
# chart.plot()  #Mac os下可用



