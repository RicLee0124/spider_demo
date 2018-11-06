#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 9:55
# @Author  : RicLee
# @Site    : 
# @File    : ProcessJson.py
# @Software: PyCharm

from urllib import request
import json


def get_data():
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=400&page_start=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    if response.getcode() == 200:
        result = response.read()
        # print(type(result))  # bytes类型
        return result


def parse_data(html):
    # 将字符串形式的json转换为dict字典
    data = json.loads(html)
    # print(type(data), data)
    movies = data['subjects']
    for movie in movies:
        print(movie['title'], movie['rate'])


if __name__ == '__main__':
    parse_data(get_data())