# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JokesPipeline(object):
    def process_item(self, item, spider):
        with open('jokes.txt','a+') as f :
            f.write('作者{} \n{}').format(item['auther'],item['content'])
        return item
