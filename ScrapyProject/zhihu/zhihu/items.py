# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class ZhihuQuestionItem(scrapy.Item):
    question_id = scrapy.Field(
        output_processor = TakeFirst()
    )
    title = scrapy.Field(
        output_processor=TakeFirst()
    )
    content = scrapy.Field(
        output_processor=Join(',')
    )
    tags = scrapy.Field(
        output_processor = Join(',')
    )
    followers = scrapy.Field(
        output_processor=TakeFirst()
    )
    viewed = scrapy.Field(

    )
    answer_num = scrapy.Field(

        output_processor = TakeFirst()
    )
    url = scrapy.Field(
        output_processor=TakeFirst()
    )

    def get_insert_sql(self):
        insert_sql = """
                insert into ZhihuQuestion(question_id,title,content,tags,followers,viewed,answer_num,url)
                values(%s ,%s,%s,%s,%s ,%s,%s,%s)
                ON DUPLICATE KEY UPDATE
                QUESTION_ID=VALUES(question_id) ,TITLE = VALUES(title) , CONTENT = VALUES(content) ,TAGS = VALUES(tags),
                FOLLOWERS=VALUES(followers),viewed=VALUES(viewed),answer_num=VALUES(answer_num),url=VALUES(url)
        """  # ON DUPLICATE KEY UPDATE 如果主键重复 则进行更新操作
        question_id = self['question_id']
        title = self['title']
        content = self['content']
        tags = self['tags']
        followers = self['followers']
        viewed = self['viewed'][1]
        answer_num = self['answer_num']
        url = self['url']

        params = (question_id,title,content,tags,followers,viewed,answer_num,url)
        return insert_sql,params