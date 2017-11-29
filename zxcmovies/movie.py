# -*- coding: utf-8 -*-

import json
import os
import time
import csv

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
        r = requests.get(url=url,headers= header)
        data = json.loads(r.text)
        item = {}
        for subject in data['subjects']:
            casts = [each.get('name') for each in subject.get('casts')]
            directors = [each.get('name') for each in subject.get('directors')]
            genres = subject.get('genres')
            if  ACTOR in directors or ACTOR in casts:
                item['directors'] = '/'.join(directors)
                item['casts'] = '/'.join(casts)
                item['genres'] = '/'.join(genres)
                item['movie_id'] = subject.get('id')
                item['title'] = subject.get('title')
                item['rate'] = subject.get('rating').get('average')
                item['year'] = subject.get('year')
                yield item
        time.sleep(2)

movie_file = 'movies.csv'
# def write2file(movies):
#     if os.path.exists('movies.json'):
#         movie_ids = read_csv('movies.json')
#
#     with open('movies.json','a',encoding='utf-8') as f:
#         for movie in movies:
#             if movie.get('movie_id') not in movie_ids:
#                 f.write(json.dumps(movie,ensure_ascii=False))
#                 f.write('\n')
#                 print("Write movie id:{} into file".format(movie.get('movie_id')))
#             else:
#                 print("Movie id:{} already in file".format(movie.get('movie_id')))

def read_csv(movie_file):
    movie_ids = []
    with open(movie_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie_ids.append(row['movie_id'])
    return movie_ids


def  write_csv(movies):
    movie_ids = []
    if os.path.exists(movie_file):
        movie_ids = read_csv(movie_file)

    with open('movies.csv','a',newline='') as csvfile:
        MOVIES_FIELDS = ['title', 'rate', 'casts', 'genres',
                         'directors', 'movie_id', 'year',
                         ]
        writer = csv.DictWriter(csvfile,fieldnames=MOVIES_FIELDS)
        writer.writeheader()

        for movie in movies:
            if movie_ids:
                if movie.get('movie_id') not in movie_ids:
                    writer.writerow(movie)
                    print("Write movie id:{} into file".format(movie.get('movie_id')))
                else:
                    print("Movie id:{} already in file".format(movie.get('movie_id')))
            else:
                writer.writerow(movie)



def main():
    movies = spider_movie()
    write_csv(movies)



if __name__ == '__main__':
    main()

