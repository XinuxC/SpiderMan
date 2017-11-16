# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from multiprocessing.dummy import Pool




class DoubanbookPipeline(object):
    def process_item(self, item, spider):
        # items = []
        # items.append(item)
        # pool = Pool(8)
        # pool.map(self.save_bookinfo, items)
        # pool.close()
        # pool.join()

        with open('books.txt','a+',encoding='utf-8') as f :
            author = item['info'].split(' / ')[0]         # [美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元
            publisher = item['info'].split(' / ')[-3]      # 钱锺书 / 人民文学出版社 / 1991-2 / 19.00
            publish_time = item['info'].split(' / ')[-2]
            price = item['info'].split(' / ')[-1]
            f.write('书名:{} '.format(item['name']))
            f.write('评分:{}\n'.format(item['rating']))
            # f.write('信息:{}\n'.format(item['info']))
            f.write('作者:{}\n'.format(author))
            f.write('出版社:{}\n'.format(publisher))
            f.write('出版时间:{}\n'.format(publish_time))
            f.write('价格:¥{}\n'.format(price))
            f.write('--------------------------------------\n')
        return item



    # def save_bookinfo(self,item):
    #     with open('books.txt','a+',encoding='utf-8') as f :
    #         author = item['info'].split('/')[0]
    #         publisher = item['info'].split('/')[1]
    #         publish_time = item['info'].split('/')[2]
    #         price = item['info'].split('/')[-1]
    #         f.write('书名:{} '.format(item['name']))
    #         f.write('评分:{}\n'.format(item['rating']))
    #         # f.write('信息:{}\n'.format(item['info']))
    #         f.write('作者:{}\n'.format(author))
    #         f.write('出版社{}\n'.format(publisher))
    #         f.write('出版时间:{}\n'.format(publish_time))
    #         f.write('价格:¥{}\n'.format(price))
    #         f.write('--------------------------------------\n')
    #     return item


