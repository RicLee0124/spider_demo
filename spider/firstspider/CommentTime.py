#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 17:41
# @Author  : RicLee
# @Site    : 
# @File    : CommentTime.py
# @Software: PyCharm

from pyecharts import Pie
import time

#  获取评论中所有评分
commentTime = []
with open('comments.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        rowplits = row.split(',')
        if len(rowplits) > 5:
            dateStr = rowplits[-1].strip('\n')
            tm = time.strptime(dateStr, '%Y-%m-%d %H:%M:%S').tm_hour
            commentTime.append(str(tm))

# 定义星级
attr = ['0-1', '1-2', '2-3', '3-4', '4-5','5-6', '6-7', '7-8', '8-9', '9-10',
        '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20',
        '20-21','21-22','22-23','23-24']

value = [
    commentTime.count('00'),
    commentTime.count('01'),
    commentTime.count('02'),
    commentTime.count('03'),
    commentTime.count('04'),
    commentTime.count('05'),
    commentTime.count('06'),
    commentTime.count('07'),
    commentTime.count('08'),
    commentTime.count('09'),
    commentTime.count('10'),
    commentTime.count('11'),
    commentTime.count('12'),
    commentTime.count('13'),
    commentTime.count('14'),
    commentTime.count('15'),
    commentTime.count('16'),
    commentTime.count('17'),
    commentTime.count('18'),
    commentTime.count('19'),
    commentTime.count('20'),
    commentTime.count('21'),
    commentTime.count('22'),
    commentTime.count('23'),
]
pie = Pie("《一出好戏》评论时间点", title_pos='center', width=900)
pie.add("", attr, value, is_label_show=True, is_legend_show=False)
pie.render('评分时间-饼图.html')