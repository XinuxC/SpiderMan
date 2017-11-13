# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import json
import codecs
import pymysql

class WeatherPipeline(object):
    def process_item(self, item, spider):
        '''
                处理每一个从SZtianqi传过来的
                item
        '''
        basedir = os.getcwd()
        filename = basedir + os.sep + 'weather.txt'
        with open(filename,'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')


        return item
