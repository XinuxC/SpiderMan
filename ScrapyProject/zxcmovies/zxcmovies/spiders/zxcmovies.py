# -*- coding: utf-8 -*-
import scrapy
from zxcmovies.items import ZxcmoviesItem


class ZxcmoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["api.douban.com"]
    start_urls = ['http://api.douban.com/v2']
    ACTOR = u'周星驰'
    urls = ['http://api.douban.com/v2/movie/search?q={周星驰}&count=20&start=' + str(n) for n in range(0, 120, 20)]
    def start_parse(self):
        yield scrapy.Request(url=self.urls,callback=self.spider_movie)


    def spider_movie(self,response):
        if not response:
            return None
        print('Download:',response.url)
        item = ZxcmoviesItem
        for subject in response['subjects']:
            casts = [each.get('name') for each in subject.get['casts']]
            if self.ACTOR in casts:
                item['casts'] = '/'.join(casts)
            genres = subject.get('genres')
            item['genres'] = '/'.join(genres)
            directors = [each.get('name') for each in subject.get('directors')]
            item['directors'] = '/'.join(directors)
            item['movie_id'] = subject.get('id')
            item['title'] = subject.get('title')
            item['rate'] = subject.get('rating').get('average')
            item['year'] = subject.get('year')

        yield item




