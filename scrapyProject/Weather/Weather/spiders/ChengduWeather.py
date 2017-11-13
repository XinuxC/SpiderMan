# -*- coding: utf-8 -*-
import scrapy
from Weather.items import WeatherItem

class ChengduweatherSpider(scrapy.Spider):
    name = 'ChengduWeather'
    allowed_domains = ['chengdu.tianqi.com']
    start_urls = ['http://chengdu.tianqi.com']

    def parse(self, response):
        items = []
        days = response.xpath('//div[@class="day7"]')
        for day in range(7):
            item = WeatherItem()
            item['date'] = response.xpath('//ul/li/b/text()').extract()[day]
            item['weekday'] = response.xpath('//ul[@class="week"]/li/span/text()').extract()[day]
            item['weather'] = response.xpath('//ul[@class="txt txt2"]/li/text()').extract()[day]
            item['wind'] = response.xpath('//ul[@class="txt"]/li/text()').extract()[day]
            highTemp = response.xpath('//div[@class="zxt_shuju"]/ul/li/span/text()').extract()[day]
            lowTemp = response.xpath('//div[@class="zxt_shuju"]/ul/li/b/text()').extract()[day]
            item['temperature'] = lowTemp + '~' +highTemp
            items.append(item)
        return items

            # yield 同样可以返回数据个pipeline
            # highTemp = response.xpath('//div[@class="zxt_shuju"]/ul/li/span/text()').extract()[day]
            # lowTemp = response.xpath('//div[@class="zxt_shuju"]/ul/li/b/text()').extract()[day]
            # yield {
            #     'date' : response.xpath('//ul/li/b/text()').extract()[day],
            #     'weekday' : response.xpath('//ul[@class="week"]/li/span/text()').extract()[day],
            #     'weather' : response.xpath('//ul[@class="txt txt2"]/li/text()').extract()[day],
            #     'wind' : response.xpath('//ul[@class="txt"]/li/text()').extract()[day],
            #     'temperature' : (lowTemp + '~' +highTemp)
            # }

