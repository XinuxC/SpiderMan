# -*- coding: utf-8 -*-
import json

import requests

header = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',

}

def spider_movie():
    ACTOR = '周星驰'
    urls = ['http://api.douban.com/v2/movie/search?q={周星驰}&count=20&start=' + str(n) for n in range(0, 120, 20)]
    for url in urls:
        r = requests.get(url=url)
        # print(r.status_code)
        data = json.loads(r.text)
        # print(data['subjects'])
        item = {}
        for subject in data['subjects']:
            casts = [each.get('name') for each in subject.get('casts')]
            # print(casts)
            if  casts and ACTOR in casts:
                item['casts'] = '/'.join(casts)
            else:
                pass
            genres = subject.get('genres')
            item['genres'] = '/'.join(genres)
            directors = [each.get('name') for each in subject.get('directors')]
            item['directors'] = '/'.join(directors)
            item['movie_id'] = subject.get('id')
            item['title'] = subject.get('title')
            item['rate'] = subject.get('rating').get('average')
            item['year'] = subject.get('year')

            yield item

if __name__ == '__main__':
    # spider_movie()
    items = spider_movie()
    for item in items:
        print(item)

