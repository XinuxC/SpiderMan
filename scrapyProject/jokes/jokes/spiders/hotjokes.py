# -*- coding: utf-8 -*-
import scrapy
from jokes.items import JokesItem

class HotjokesSpider(scrapy.Spider):
    name = "hotjokes"
    allowed_domains = ["qiushibaike.com"]
    start_urls = []

    for i in range(1,3):
        url = 'https://www.qiushibaike.com/8hr/page/%s/' % i
        start_urls.append(url)

    def parse(self, response):
        item = JokesItem()

        jokes = response.xpath('//*[@id="content-left"]/div')

        for joke in jokes:
            item['auther'] = joke.xpath('.//h2/text()').extract()[0]
            item['content'] = joke.xpath('.//div[@class="content"]/span/text()').extract()[0].strip()
            yield item

