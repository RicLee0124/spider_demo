#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 17:08
# @Author  : RicLee
# @Site    : 
# @File    : WordCloud.py
# @Software: PyCharm

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# 获取所有评论内容
comments = []
with open('comments.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        rowsplits = row.split(',')
        if len(rowsplits)>3:
            comment = row.split(',')[3]
            if comment != '':
                comments.append(comment)

# 设置分词
comment_after_split = jieba.cut(str(comments), cut_all=False)
words = ' '.join(comment_after_split)  # 以空格进行拼接
# print(words)

# 设置屏蔽词汇
stopwords = STOPWORDS.copy()
stopwords.add('电影')
stopwords.add('一出')
stopwords.add('好戏')
stopwords.add('有点')

# 导入背景图
bg_image = plt.imread('love.jpg')

# 设置词云参数
wc = WordCloud(width=1024, height=768, background_color='white', mask=bg_image, stopwords=stopwords, max_font_size=400,
               random_state=50,font_path='STKAITI.TTF')
# 将分词后数据导入云图
wc.generate_from_text(words)
#  绘制图像
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴
plt.show()  # 显示图像
# 保存图像到文件
wc.to_file('词云图.jpg')