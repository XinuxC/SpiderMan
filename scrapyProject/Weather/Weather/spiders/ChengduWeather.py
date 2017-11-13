# -*- coding: utf-8 -*-
import scrapy
from Weather.items import WeatherItem

class ChengduweatherSpider(scrapy.Spider):
    name = 'ChengduWeather'
    allowed_domains = ['chengdu.tianqi.com']
    start_urls = ['http://chengdu.tianqi.com/']

    def parse(self, response):
        items = []
        days = response.xpath('//div[@class="day7"]')
        for day in days:
            item = WeatherItem()
            item['date'] = day.xpath('./ul/li/b/text()').extract()[0]
            item['weekday'] = day.xpath('./ul[@class="week"]/li/span/text()').extract()[0]
            item['weather'] = day.xpath('./ul[@class="txt txt2"]/li/text()').extract()[0]
            item['wind'] = day.xpath('./ul[@class="txt"]/li/text()').extract()[0]
            highTemp = day.xpath('./div[@class="zxt_shuju"]/ul/li/span/text()').extract()[0]
            lowTemp = day.xpath('./div[@class="zxt_shuju"]/ul/li/b/text()').extract()[0]
            item['temperature'] = lowTemp + '~' +highTemp
            items.append(item)
        return items
