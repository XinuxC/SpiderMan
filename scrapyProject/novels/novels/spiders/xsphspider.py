# -*- coding: utf-8 -*-
import scrapy
from .sjzh import get_tit_num,Cn2An
from novels.items import NovelsItem

class XsphspiderSpider(scrapy.Spider):
    name = 'xsphspider'
    allowed_domains = ['qu.la']
    start_urls = ['http://www.qu.la/paihangbang/']
    novel_list= []

    def parse(self, response):
        # 找到各类小说排行榜名单
        books = response.xpath('//div[@class="index_toplist mright mbottom"]')

        #找到每一类小说排行榜的每一本小说下载链接
        for book in books:
            links = book.xpath('.//div[2]/div[2]/ul/li')
            for link in links:
                url = response.urljoin(link.xpath('.//a/@href').extract()[0])
                self.novel_list.append(url)

        #简单去重
        self.novel_list = list(set(self.novel_list))

        for novel in self.novel_list:
            yield scrapy.Request(novel,callback=self.get_chapter_url)

    def get_chapter_url(self,response):
            #'''找到章节链接'''
        chapter_urls = response.xpath('//dd/a/@href').extract()

        for url in chapter_urls:
            yield scrapy.Request('http://www.qu.la'+url,callback=self.get_text)

    def get_text(self,response):
          #   '''
          #   找到每一章小说的标题和正文
          #   并自动生成id字段，用于表的排序
          # #  '''
        item = NovelsItem()
        #小说名
        item['bookname'] = response.xpath('.//div[@class="con_top"]/a[2]/text()').extract()[0]
        #章节名
        title = response.xpath('//h1/text()').extract()[0]
        item['title'] = title

        item['order_id'] = Cn2An(get_tit_num(title))

        #正文部分需要特殊处理
        body = response.xpath('.//div[@id="content"]/text()').extract()

        text = ''.join(body).strip().replace('\u3000','')
        item['body'] = text
        return item


