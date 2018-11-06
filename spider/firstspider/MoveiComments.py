#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 9:56
# @Author  : RicLee
# @Site    : 
# @File    : MoveiComments.py
# @Software: PyCharm

from urllib import request
import json
from datetime import datetime, timedelta
import time


# 获取数据
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    if response.getcode() == 200:
        return response.read()


# 处理数据
def parse_data(html):
    data = json.loads(html)['cmts']
    comments = []
    for item in data:
        comment = {
            'id': item['id'],
            'nickName': item['nickName'],
            'cityName': item['cityName'] if 'cityName' in item else '',  # 处理cityName不存在情况
            'content': item['content'].replace('\n', ' '),  # 处理评论内容换行的情况
            'score': item['score'],
            'startTime': item['startTime']
        }
        comments.append(comment)
    return comments


# 存储数据到文本文件
def save_to_txt():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前时间
    end_time = '2018-08-10 00:00:00'  # 结束时间
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset=0&startTime=' + start_time.replace(
            ' ', '%20')
        try:
            html = get_data(url)
        except:
            time.sleep(0.3)  #网站有反爬虫机制，频繁访问请求会被拒绝，当被拒绝停止一秒再访问
            html = get_data(url)
        else:
            time.sleep(0.02) #降低访问频率

        comments = parse_data(html)
        print(comments)

        start_time = comments[14]['startTime']  # 末尾评论时间
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=1)  # 向前减１秒，防止获取到重复数据
        start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')

        for item in comments:
            with open('comments.txt', mode='a', encoding='utf-8') as f:
                f.write(str(item['id']) + ',' + item['nickName'] + ',' + item['cityName'] + ',' + item[
                    'content'] + ',' + str(item['score']) + ',' + item['startTime'] + '\n')


if __name__ == '__main__':
    # url = 'http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset=15&startTime=2018-09-01%2011%3A10%3A00'
    # comments = parse_data(get_data(url))
    # print(comments)
    save_to_txt()