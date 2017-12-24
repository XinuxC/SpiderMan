#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : getproxies.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/12/24
# @Desc  :
import requests,pymysql

class GetProxyIP(object):
    def __init__(self):
        self.conn = pymysql.Connect(host="219.234.147.220", user="root", passwd="mysqlforgxsn@210", db="pymysql",
                                    charset="utf8mb4")
        self.cursor = self.conn.cursor()

    def _delete_ip(self, ip):
        sql = """
            delete from proxy where ip = '{0}'
        """.format(ip)

        self.cursor.execute(sql)
        self.conn.commit()

    def _get_random_proxy(self):
        sql = """
            select ip ,port from proxy ORDER BY RAND() LIMIT 1;
        """
        self.cursor.execute(sql)
        for ips in self.cursor.fetchall():
            ip = ips[0]
            port = ips[1]

            if self._is_valid(ip, port):
                # print('proxy alives')
                # print(proxies)
                return 'http://%s:%s' % (ip, port)
            else:
                self._delete_ip(ip)
                return self._get_random_proxy()
        self.conn.close()

    def _is_valid(self, ip, port):
        url = "https://www.baidu.com"
        proxies = {
            'http': 'http://%s:%s' % (ip, port),
            # 'https':'http://%s:%s'%(ip,port)
        }
        try:
            r = requests.get(url, proxies=proxies)

        except Exception as e:
            print("invalid ip")
            return False
        else:
            status = r.status_code
            if status >= 200 and status < 400:
                return True
            else:
                return False
