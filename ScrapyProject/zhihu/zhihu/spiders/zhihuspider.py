# -*- coding: utf-8 -*-



import scrapy
import json
import re
import time
import os

from PIL import Image
from zhihu.items import  ZhihuQuestionItem
from scrapy.loader import ItemLoader


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuspider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/','https://www.zhihu.com/topic','https://www.zhihu.com/explore']

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Host':'www.zhihu.com',
    }

    def start_requests(self):
        with open('cookies.txt') as f:
            cookies = json.load(f)
        return [scrapy.Request('https://www.zhihu.com/',headers= self.headers,cookies = cookies,callback=self.is_login)]
        # return [scrapy.Request('https://www.zhihu.com/',headers= self.headers,callback=self.login)]

    def login(self,response):
        pattern = r'name="_xsrf" value="(.*?)"/>'
        xsrf = re.findall(pattern, response.text, re.S | re.I)
        if xsrf[0]:
            post_data = {
                '_xsrf':xsrf[0],
                'phone_num':'18200590129',
                'password':'chenyuejun900129',
            }

            t = str(int(time.time() * 1000))
            # 手机登录验证码地址
            captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
            # captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login&lang=cn"  # 倒立验证码图片地址
            yield scrapy.Request(captcha_url, headers=self.headers, meta={'post_data':post_data}, callback=self.captcha_login)

    def captcha_login(self,response):
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = response.meta.get('post_data')

        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
        captcha = input('请输入验证码:')
        post_data['captcha'] = captcha

        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.is_login,
        )]

    def is_login(self,response):
        # login_info = json.loads(response.text)
        # if 'msg' in login_info and login_info['msg'] == "登录成功":
        #     for url in self.start_urls:
        #         yield scrapy.Request(url=url,headers=self.headers,dont_filter=True)
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.headers, dont_filter=True)

    def parse(self, response):
        # 提取所有问题url,跟踪进一步爬取
        pattern = r'<a target="_blank" data-za-detail-view-element_name="Title" href="(/question/\d+)/answer/\d+" .*?'
        result = re.findall(pattern,response.text)
        if result:
            for url in result:
                url = response.urljoin(url)
                yield scrapy.Request(url=url,headers=self.headers,callback=self.parse_question)
        else:
            yield scrapy.Request(url=response.url,headers=self.headers,callback=self.parse)

    def parse_question(self,response):
        pattern = re.compile('.*zhihu.com/question/(\d+)')
        question_id = pattern.findall(response.url)
        item_loader = ItemLoader(item=ZhihuQuestionItem(), response=response)
        item_loader.add_value('question_id',question_id)  # question_id
        item_loader.add_css('title','h1.QuestionHeader-title::text')  # title
        item_loader.add_css('content','.QuestionHeader-detail ::text')  # content
        item_loader.add_css('tags','.TopicLink ::text')  # tags
        item_loader.add_css('followers','.QuestionFollowStatus .NumberBoard-value::text')  # followers 第一个数作为关注数
        item_loader.add_css('viewed','.QuestionFollowStatus .NumberBoard-value::text')  # viewed  第二个数作为浏览数
        item_loader.add_css('answer_num','h4.List-headerText ::text')  # answer_num
        item_loader.add_value('url',response.url)  # url


        qustion_item = item_loader.load_item()
        yield qustion_item


