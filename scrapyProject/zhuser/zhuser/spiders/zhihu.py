# -*- coding: utf-8 -*-
import json

import scrapy
from zhuser.items import ZhuserItem

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    # start_urls = ['http://www.zhihu.com/']
    # 用户主页
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    # 他关注的人
    follow_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&amp;offset={offset}&amp;limit={limit}'
    # 关注他的人
    follower_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&amp;offset={offset}&amp;limit={limit}'
    # 起始用户
    start_user = 'excited-vczh'
    # 用户主页用信息
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,' \
                 'following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,' \
                 'articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,' \
                 'marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,' \
                 'sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,' \
                 'vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,' \
                 'allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    # 关注和被关注用信息
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'


    def start_requests(self):
        yield scrapy.Request(self.user_url.format(user=self.start_user,include=self.user_query),
                             callback=self.parse_user)
        yield scrapy.Request(self.follow_url.format(user=self.start_user,include=self.follows_query,limit=20,offset=0),
                             callback=self.parse_follows)
        yield scrapy.Request(self.follower_url.format(user=self.start_user,include=self.followers_query,limit=20,offset=0),
                             callback=self.parse_followers)

    def parse_user(self, response):
        # print(response.text)
        result = json.loads(response.text)
        item = ZhuserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item
        yield scrapy.Request(self.follow_url.format(user=result.get('url_token'),
                                                    include=self.follows_query,limit=20,offset=0),
                                                    callback=self.parse_follows)
        yield scrapy.Request(self.follower_url.format(user=result.get('url_token'),
                                                      include=self.followers_query,limit=20,offset=0),
                                                      callback=self.parse_followers)
    def parse_follows(self,response):
        # print(response.text)
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),
                                     callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(next_page,callback=self.parse_follows)

    def parse_followers(self,response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),
                                     callback=self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(next_page,callback=self.parse_followers)

