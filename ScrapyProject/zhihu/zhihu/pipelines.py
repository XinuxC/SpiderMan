# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item


#利用twisted连接池异步插入数据库
from twisted.enterprise import adbapi
import pymysql
class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparams = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
        )

        dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        return cls(dbpool)


    def process_item(self,item,spider):
        #使用twisted将插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error,item,spider)

    def handle_error(self,failure,item,spider):
        # 处理异步插入异常,异步插入可能会有重复,这里先只是打印
        print(failure)

    def do_insert(self,cursor,item):
        # 执行具体插入
        insert_sql , params = item.get_insert_sql()
        cursor.execute(insert_sql,params)

        return item
