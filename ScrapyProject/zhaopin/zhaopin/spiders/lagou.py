# -*- coding: utf-8 -*-
import datetime
import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from zhaopin.items import ZhaopinItem,ZhaopinItemLoader

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Python/']

    rules = (
        Rule(LinkExtractor(allow=(r'zhaopin/.*',)),follow=True),
        Rule(LinkExtractor(allow=(r'gongsi/j\d+.html',)),follow=True),
        Rule(LinkExtractor(allow=(r'jobs/\d+.html',)), callback='parse_item', follow=True),
    )

    # def parse_start_url(self):
         # return []

    # def process_results(self, response, results):
    #     return results

    def start_requests(self):
        # 使用cookie,登录后直接开始请求start_urls
        with open('cookies.txt') as f:
            cookies = json.load(f)
        return [scrapy.Request('https://www.lagou.com/zhaopin/Python/',cookies = cookies)]

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        item_loader = ZhaopinItemLoader(item=ZhaopinItem(),response=response)
        item_loader.add_value('url',response.url)  # url
        item_loader.add_value('url_object_id',response.url)  # url md5
        item_loader.add_css('title','.job-name::attr(title)')
        item_loader.add_css('company','.job_company dt a img::attr(alt)')
        item_loader.add_css('salary','.job_request .salary ::text')
        item_loader.add_xpath('city','//dd[@class="job_request"]/p/span[2]/text()')
        item_loader.add_xpath('working_years','//dd[@class="job_request"]/p/span[3]/text()')
        item_loader.add_xpath('degree','//dd[@class="job_request"]/p/span[4]/text()')
        item_loader.add_xpath('job_type','//dd[@class="job_request"]/p/span[5]/text()')
        item_loader.add_css('release_time','.publish_time ::text')
        item_loader.add_css('job_tags','.position-label.clearfix li ::text')  ##
        item_loader.add_css('job_advantage','.job-advantage p ::text')
        item_loader.add_xpath('job_desc','//dd[@class="job_bt"]/div/p/text()|//dd[@class="job_bt"]/div/ul/li/text()')  ##
        item_loader.add_css('work_addr','.work_addr ::text')
        item_loader.add_css('company_page','.job_company a::attr(href)')
        item_loader.add_value('crawl_time',datetime.datetime.now())
        item_loader.add_value('update_time',datetime.datetime.now())

        job_items = item_loader.load_item()
        yield job_items

        next_page = response.xpath('//div[@class="pager_container"]/a[last()]/@href')
        if next_page:
            yield scrapy.Request(next_page,callback=self.parse_item)



        # return i
