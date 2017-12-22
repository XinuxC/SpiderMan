# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join
from scrapy.loader import ItemLoader
from zhaopin.utils import addr_strip,remove_backlash,url_md5,get_time
from w3lib.html import remove_tags


class  ZhaopinItemLoader(ItemLoader):
    # 自定义itemloader,默认获取列表第一个内容
    default_output_processor = TakeFirst()

class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    url_object_id = scrapy.Field(
        input_processor = MapCompose(url_md5)
    )
    url = scrapy.Field()
    company = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field(
        input_processor= MapCompose(remove_backlash)
    )
    working_years = scrapy.Field(
        input_processor=MapCompose(remove_backlash)
    )
    degree = scrapy.Field(
        input_processor=MapCompose(remove_backlash)
    )
    job_type = scrapy.Field()
    release_time = scrapy.Field(
        input_processor=MapCompose(get_time)
    )
    job_tags = scrapy.Field(
        output_processor = Join(',')
    )
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field(
        output_processor=Join('')
    )
    work_addr = scrapy.Field(
        input_processor = MapCompose(addr_strip),
        output_processor = Join('')
    )
    company_page = scrapy.Field(
        output_processor=Join(',')
    )
    crawl_time = scrapy.Field()
    update_time = scrapy.Field()

    def get_insert_sql(self):
        inster_sql = '''
            insert into JobInfo(url_object_id,url,company,title,salary,city,working_years,degree,job_type,release_time,
                                 job_tags,job_advantage,job_desc,work_addr,company_page,crawl_time,update_time)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
            url_object_id = values(url_object_id),url = values(url),company = values(company),title = values(title),
            salary = values(salary),city = values(city),working_years = values(working_years),degree = values(degree),
            job_type = values(job_type),release_time=values(release_time),job_tags = values(job_tags),
            job_advantage = values(job_advantage),job_desc=values(job_desc),work_addr=values(work_addr),
            company_page = values(company_page),update_time=values(update_time)  
        '''                                     ## ↑↑↑ 如果是更新的话就不插入新的crawl_time,只插入新的update_time
        url_object_id = self['url_object_id']
        url = self['url']
        company = self['company']
        title = self['title']
        salary = self['salary']
        city = self['city']
        working_years = self['working_years']
        degree = self['degree']
        job_type = self['job_type']
        release_time = self['release_time']
        job_tags = self['job_tags']
        job_advantage = self['job_advantage']
        job_desc = self['job_desc']
        work_addr = self['work_addr']
        company_page = self['company_page']
        crawl_time = self['crawl_time']
        update_time = self['update_time']

        params = (url_object_id,url,company,title,salary,city,working_years,degree,job_type,release_time,job_tags,
                  job_advantage,job_desc,work_addr,company_page,crawl_time,update_time)

        return inster_sql,params