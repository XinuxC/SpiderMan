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
          处理每一个从Chengdutianqi传过来的item
        '''
        basedir = os.getcwd()
        filename = basedir + os.sep + 'weather.txt'
        with open(filename,'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['weekday'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')
        return item

# 爬取的信息保存到json方便其他程序员调用
class W2json(object):
    def process_item(self,item,spider):
        basedir = os.getcwd()
        filename = basedir + os.sep + 'weather.json'
        with open(filename,'a',encoding='utf-8') as f :
            line = json.dumps(dict(item),ensure_ascii=False) + '\n'
            f.write(line)
        return item

# 数据存储到MySQL
class W2mysql(object):
    def open_spider(self, spider):  # 爬虫打开的时候做的操作
        self.conn = pymysql.connect(
            host='219.234.147.218',
            port=23306,
            user='root',
            passwd='yaojing0129',
            db='scrapyDB',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def close_spider(self, spider):  # 爬虫结束的时候做的操作
        self.conn.close()

    def process_item(self,item,spider):
        date = item['date']
        weekday = item['weekday']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']

        # conn = pymysql.connect(
        #     host='219.234.147.218',
        #     port=23306,
        #     user='root',
        #     passwd='yaojing0129',
        #     db='scrapyDB',
        #     charset='utf8mb4',
        #     cursorclass=pymysql.cursors.DictCursor)
        try:
            with self.conn.cursor() as cursor:
                sql = '''INSERT INTO weather(date,weekday,temperature,weather,wind)
                        VALUES (%s, %s,%s,%s,%s)'''
                ## excute 的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute(sql,(date,weekday,temperature,weather,wind))
            self.conn.commit()
        except:
            raise ConnectionError
        # finally:
        #     self.conn.close()
        return item

