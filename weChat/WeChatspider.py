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

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
from  collections import Counter
#login
itchat.login()
# 获取朋友列表
friends = itchat.get_friends(update=True)
# send msg
# itchat.send_image('D:\python\weChat\signature.jpg')

#获取头像
def save_headimg():
    num = 1
    for friend in friends:
        img = itchat.get_head_img(friend['UserName'])
        fileImage = open('headimg'+os.sep+str(num)+'.jpg','wb')
        fileImage.write(img)
        fileImage.close()
        num += 1

#生成照片墙
import math
def imaWall():
    img_list = os.listdir('headimg')
    size = int(math.sqrt(float(720*720)/len(img_list)))
    lines = int(640/size)
    image = Image.new('RGBA',(790,790))  # If it's got an alpha channel that you want to preserve,
                                         # PNG is really the only reasonable choice.
                                         # Alternately you can flatten it to a RGB image and save as a JPEG.
    x = y = 0
    for i in range(1,len(img_list)+1):
        try:
            img = Image.open('headimg'+os.sep+str(i)+'.jpg')
        except IOError:
            print("error")
        else:
            img = img.resize((size,size),Image.ANTIALIAS)
            image.paste(img,(x * size,y * size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    image.save('HeadsWall.png')

import pyecharts
#获取位置
def get_location():
    locations = []
    for friend in friends[:]:
        locations.append(friend['City'])
    provinces = set(locations)
    data = []
    for i in provinces:
        data.append((i,locations.count(i)))
    print(data)
    # data =[('江苏', 2), ('Ferrara', 1), ('北京', 28), ('黑龙江', 11), ('重庆', 1), ('上海', 8), ('Van', 1), ('湖南', 1), ('Antalya', 1), ('Barcelona', 1), ('Dubayy', 1), ('海南', 1), ('Male Atoll', 1), ('Victoria', 2), ('四川', 96), ('吉林', 2), ('North Thiladhunmathi', 1), ('Douro', 1), ('福建', 1), ('辽宁', 1), ('安徽', 1), ('St.Gallen', 1), ('广西', 1), ('Ontario', 1), ('New South Wales', 1), ('浙江', 1), ('Wong Tai Sin', 1), ('Fukuoka', 1), ('广东', 6), ('西藏', 1)]
    # data =[('江苏', 2), ('北京', 28), ('黑龙江', 11), ('重庆', 1), ('上海', 8), ('湖南', 1),  ('海南', 1), ('四川', 96), ('吉林', 2), ('福建', 1), ('辽宁', 1), ('安徽', 1),  ('广西', 1),  ('浙江', 1),  ('广东', 6), ('西藏', 1)]
    geo = pyecharts.Geo("朋友分布", "cordinates and counts", title_color="#fff", title_pos="center",
              width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value,maptype='china', type="effectScatter",
            visual_text_color="#fff",is_random=True, effect_scale=5, is_legend_show=False)
    geo.render('location.html')

#性别统计
#性别conver to chart
def to_charts():
    male = female = others = 0
    total = len(friends)
    for i in friends[:]:
        sex = i['Sex']
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            others += 1
    attr = ["男", "女", "妖"]
    v1 = [round(float(male)/total*100,2), round(float(female)/total*100,2), round(float(others)/total*100,2)]
    #条状图
    # bar = pyecharts.Bar("性别统计")
    # bar.add("male/female/others", attr, v1, is_stack=True)
    # bar.render()
    #饼图-圆环图
    pie = pyecharts.Pie("比例图",title_pos='right')
    pie.add("",attr,v1,radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
    pie.render('Sex.html')

#获取好友个性签名 做成词云
def to_wl_pic():
    signatures = []
    for i in friends:
        # signature = i['Signature']
        signature= i['Signature'].strip().replace("span","").replace("class","").replace("emoji","")
        rep = re.compile("1f\d.+")
        signature = rep.sub("",signature)
        signatures.append(signature)
    # print(signature)

    #拼接字符串
    text = ''.join(signatures)
    #jieba分词
    wordlist = jieba.cut(text,cut_all=True)
    # wordlist = jieba.cut(text)
    wl_space_split = " ".join(list(wordlist))

    #wordcloud词云
    basename = os.path.abspath('20171120223350.jpg')
    background = np.array(Image.open(basename))
    my_wordCloud = WordCloud(background_color="white",
                             max_words = 5000,  # 词云显示最大词数
                             mask = background,  # 设置背景
                             max_font_size=100,  # 字体最大值
                             random_state=42,
                             font_path='STXINGKA.TTF',  # 设置字体
                             width=1000,
                             height=860,  # 设置图片默认大小
                             margin=2).generate(wl_space_split)
    image_color = ImageColorGenerator(background)
    plt.imshow(my_wordCloud.recolor(color_func=image_color))
    plt.figure()
    plt.imshow(my_wordCloud)
    plt.axis("off")
    plt.show()
    my_wordCloud.to_file('sgnMost.jpg')


if __name__ == '__main__':
    save_headimg()
    imaWall()
    get_location()
    to_wl_pic()
    to_charts()
    input = ("press enter to exit")