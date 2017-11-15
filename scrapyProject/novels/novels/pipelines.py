# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class NovelsPipeline(object):
    def process_item(self, item, spider):
        name = item['bookname']
        order_id = item['order_id']
        body = item['body']
        title = item['title']
        conn = pymysql.connect(
            host = '219.234.147.218',
            port = 23306,
            user = 'root',
            passwd = 'yaojing0129',
            db = 'scrapyDB',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        try:
            with conn.cursor() as cursor:
                sql1 = 'create table if not exists %s(id int,zjm varchar(20),body text)' % name
                sql = 'insert into %s values(%d,\'%s\',\'%s\')' % (name,order_id,title,body)
                cursor.execute(sql1)
                cursor.execute(sql)

            #提交本次插入记录
            conn.commit()
        finally:
            conn.close()
        # with open('%s.txt' % name ,'a+') as f :
        #     f.write(order_id+' '+title+'\n')
        #     f.write(body+'\n')
            return item
