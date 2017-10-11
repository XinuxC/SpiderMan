#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : cityWeather.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/9/19
# @Desc  :


from city import city
import requests
import json
# for k,v in city.items():
#     print(k,':',v)


def queryWeather():
    cityName = input('请输入城市名:\n')
    cityCode = city.get(cityName)
    if cityCode:
        try:
            url = 'http://d1.weather.com.cn/dingzhi/%s.html' % cityCode
            urlHeaders = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': 'http://www.weather.com.cn',
                'Host': 'd1.weather.com.cn'
            }
            req = requests.get(url, headers=urlHeaders, timeout=5)
            req.encoding = 'utf8'
            # print(req.text)
            # print(type(req.text))
            content = req.text.partition(';')
            temp_c = content[0]
            temp_data = temp_c.split('=')[1]
            # print(type(temp_data))
            data = json.loads(temp_data)
            # print(data)
            # print(type(data))
            result = data['weatherinfo']
            # print(result)
            # print(type(result))
            city_temp = ('%s\n%s°C ~%s°C\n%s') % (
                result['cityname'], result['tempn'], result['temp'], result['weather'])
            print(city_temp)
        except:
            print('查询失败')
    else:
        print('没有找到该城市')


if __name__ == '__main__':
    queryWeather()
    input('按回车退出')
