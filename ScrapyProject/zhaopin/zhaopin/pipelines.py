# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import pymysql

class ZhaopinPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.db_pool = dbpool

    @classmethod
    def from_settings(cls, settings):
        db_params = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
        )

        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool)

    def process_item(self,item,spider):
        # 使用twisted将插入变成异步执行
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        # 处理异步插入异常,异步插入可能会有重复,这里先只是打印
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
