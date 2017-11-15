# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanbookPipeline(object):
    def process_item(self, item, spider):
        with open('books.txt','a+',encoding='utf-8') as f :
            f.write('书名:{}\n'.format(item['name']))
            f.write('评分:{}\n'.format(item['rating']))
            f.write('信息:{}\n'.format(item['info']))
        return item
