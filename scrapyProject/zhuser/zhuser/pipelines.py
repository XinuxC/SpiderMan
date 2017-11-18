# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ZhuserPipeline(object):
    def process_item(self, item, spider):
        name = item['name']
        url = item['url']
        url_token = item['url_token']
        headline = item['headline']
        answer_count = item['answer_count']
        articles_count = item['articles_count']
        follower_count = item['follower_count']
        with open('users.txt','a+') as f:
            f.write('用户:{name},答题数:{answer_count},文章数:{articles_count},粉丝数:{follower_count}\n'.format(name=name,
                                                                                                      answer_count=answer_count,
                                                                                                      articles_count=articles_count,
                                                                                                      follower_count=follower_count))
        return item



class UserToMysql(object):
    def process_item(self,item,spider):
        name = item['name']
        url = item['url']
        url_token = item['url_token']
        headline = item['headline']
        answer_count = item['answer_count']
        articles_count = item['articles_count']
        follower_count = item['follower_count']
        self.conn = pymysql.connect(
                               host='localhost',
                               port=3306,
                               user='root',
                               passwd='root',
                               db='scrapydb',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.conn.cursor() as cur:
                sql= 'insert into zhuser(name,url,url_token,headline,answer_count,article_count,follower_count) ' \
                     'values(\'%s\',\'%s\',\'%s\',\'%s\',\'%d\',\'%d\',\'%d\')' % (name,url,url_token,headline,answer_count,articles_count,follower_count)

                cur.execute(sql)

            self.conn.commit()
        finally:
            self.conn.close()
        return item