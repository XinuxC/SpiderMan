# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import time


urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]


def get_music_info(url):
    r = requests.get(url)
    # r.encoding='utf-8'
    soup = BeautifulSoup(r.text,'html.parser')
    datas = soup.select('.pl2')
    songs = {}
    for item in datas:
        songs['name'] = item.a.text.strip().split('\n')[0]
        songs['singer'] = item.p.string.split('/')[0].strip()
        songs['time'] = item.p.string.split('/')[1].strip()
        songs['type'] = item.p.string.split('/')[-1].strip()

        yield songs
    time.sleep(2)

def write_to_csv(songs):
    with open('MusicTop250.csv','a',newline='') as csvfile:
        Field_Name = ['name','singer','time','type']
        writer = csv.DictWriter(csvfile,fieldnames=Field_Name)
        writer.writeheader()
        for item in songs:
            writer.writerow(item)
            print('Writing song {} into file'.format(item['name']))

def main():
    for url in urls:
        songs = get_music_info(url)
        write_to_csv(songs)


if __name__ == '__main__':
    main()