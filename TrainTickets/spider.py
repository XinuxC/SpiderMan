#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : spider.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/11/30
# @Desc  :


import re
import json

import requests

def get_stations():
    #关闭https证书验证警告
    requests.packages.urllib3.disable_warnings()
    # 12306的城市名和城市代码js文件url
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
    r = requests.get(url,verify=False)

    # pattern1 = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    pattern = u'@\w{3}\|(.*?)\|([A-Z]+)'
    result = re.findall(pattern,r.text)
    stations = json.dumps(dict(result))
    # print(stations)
    with open('stations.py','w',encoding='utf-8') as f :
        f.write('station_dict = ')
        f.write(stations)


def get_query_info():
    from stations import station_dict

    date = input("日期:")
    from_station = input("出发站:")
    to_station= input("终点站:")
    '''
    查询两站之间的火车票信息

    输入参数： <date> <from> <to>

    12306 api:
    'https://kyfw.12306.cn/otn/leftTicket/query?
    leftTicketDTO.train_date=2017-07-18&
    leftTicketDTO.from_station=NJH&
    leftTicketDTO.to_station=SZH&
    purpose_codes=ADULT'

    '''
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?' \
          'leftTicketDTO.train_date={}&' \
          'leftTicketDTO.from_station={}&' \
          'leftTicketDTO.to_station={}&' \
          'purpose_codes=ADULT'.format(date,station_dict.get(from_station),station_dict.get(to_station))
    # print(url)
    return url


def query_train_info(url):
    '''
        查询火车票信息：
        返回 信息查询列表
        '''
    # 关闭https证书验证警告
    requests.packages.urllib3.disable_warnings()

    # key：城市名 value：城市代码
    from stations import station_dict
    code_dict = {v: k for k, v in station_dict.items()}

    info_list = []
    try:
        r = requests.get(url,verify=False)
        raw_trains = r.json()['data']['result']
        # print(raw_trains)
        for row_train in raw_trains:
            data = row_train.split('|')
            # print(data)
            # 车次号码:
            train_no = data[3]
            # 出发站
            from_station_code = data[4]
            from_station_name = code_dict[from_station_code]
            # 终点站
            to_station_code = data[5]
            to_station_name = code_dict[to_station_code]
            # 出发时间
            start_time = data[8]
            # 到达时间
            arrive_time = data[9]
            # 总耗时
            total_time = data[10]
            # 一等座
            first_class_set = data[30] or '--'
            # 二等座
            second_class_seat = data[30] or '--'
            # 软卧
            soft_sleep = data[23] or '--'
            # 硬卧
            hard_sleep = data[28] or '--'
            # 硬座
            hard_seat = data[29] or '--'
            # 无座
            no_seat = data[26] or '--'

            # 打印查询结果
            info = ('车次:{} 出发站:{} 目的地:{} 发车时间:{} 到达时间:{} 时长:{} 座位情况： 一等座：「{}」 二等座：「{}」 软卧：「{}」 硬卧：「{}」 硬座：「{}」 无座：「{}」\n'.format(
                train_no,from_station_name,to_station_name,start_time,arrive_time,total_time,first_class_set,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat
            ))
            print(info)
            info_list.append(info)
        return info_list
    except:
        return ' 输出信息有误，请重新输入'

def main():
    url= get_query_info()
    query_train_info(url)


if __name__ == '__main__':
    main()
