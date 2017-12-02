# -*- coding: utf-8 -*-
import scrapy
from doubanbook.items import DoubanbookItem
from scrapy_redis.spiders import RedisSpider

class DoubanbookspiderSpider(scrapy.Spider):
# class DoubanbookspiderSpider(RedisSpider):
    name = "doubanbookspider"
    allowed_domains = ["douban.com"]
    # redis_key = 'doubanbookspider:start_urls'
    start_urls = ['https://book.douban.com/top250']
    url_list = []
    def parse(self, response):
        yield scrapy.Request(response.url,callback=self.parse_books)

        for page_url in response.xpath('//div[@class="paginator"]/a/@href').extract():
            yield scrapy.Request(page_url,callback=self.parse_books)

    def parse_books(self,response):
        # item = DoubanbookItem()
        books = response.xpath('//tr[@class="item"]')
        for book in books:
            item = DoubanbookItem()
            item['name'] = book.xpath('.//a/@title').extract()[0]
            item['info'] = book.xpath('.//p[1]/text()').extract()[0].strip()
            item['rating'] = book.xpath('.//td[2]/div[2]/span[@class="rating_nums"]/text()').extract()[0]
            yield item
        # return item  #都是返回，yield不终止程序，return直接函数就结束了
