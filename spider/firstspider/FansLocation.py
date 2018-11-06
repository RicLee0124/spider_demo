#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 15:01
# @Author  : RicLee
# @Site    : 
# @File    : FansLocation.py
# @Software: PyCharm

from collections import Counter
from pyecharts import Geo
import json
from pyecharts import Bar


def render():
    # 获取所有城市信息
    cities = []
    with open('comments.txt', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows:
            rowsplits = row.split(',')
            if len(rowsplits)>3:
                city = rowsplits[2]
                if city != '':
                    cities.append(city)

    # 对城市数据和坐标文件中的地名进行处理
    handle(cities)

    # 统计每个城市出现的次数
    # data = []  # [('南京',25),('北京',59)]
    # for city in set(cities):
    #     data.append((city, cities.count(city)))
    data = Counter(cities).most_common()

    # 根据城市数据生成地理坐标图
    geo = Geo(
        "《一出好戏》粉丝位置分布",
        "数据来源：猫眼",
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59",
    )
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        visual_range=[0, 3500],
        visual_text_color="#fff",
        symbol_size=15,
        is_visualmap=True,
    )
    geo.render('粉丝位置分布.html')

    # 根据城市数据生成柱状图
    cities_top20 = Counter(cities).most_common(20)  # 返回出现次数最多的20条
    bar = Bar("《一出好戏》粉丝来源排行榜TOP20", '数据来源：猫眼', title_pos='center', width=1200, height=600)
    attr, value = bar.cast(cities_top20)
    bar.add("", attr, value)
    bar.render('粉丝来源排行榜-柱状图.html')


# 处理地名数据，解析坐标文件中找不到地名的问题
def handle(cities):
    with open(
            'D:\\python3 workspace\\spider\\venv\\Lib\\site-packages\\pyecharts\\datasets\\city_coordinates.json',
            mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())  # 将str转换为dict

    # 循环判断处理
    data_new = data.copy()  # 复制一份地名数据
    for city in set(cities):
        count = 0
        for k in data:
            count += 1
            if k == city:
                break
            if k.startswith(city):  # 处理简写的地名，如南京市 简写为 南京
                data_new[city] = data[k]
                break
            if k.startswith(city[0:-1]) and len(city) >= 3:  # 处理行政变更的地名，如溧水县 改为 溧水区
                data_new[city] = data[k]
                break
        # 处理不存在的情况
        if count == len(data):
            while city in cities:
                cities.remove(city)
    # print(len(data), len(data_new))

    # 写入覆盖坐标文件
    with open(
            'D:\\python3 workspace\\spider\\venv\\Lib\\site-packages\\pyecharts\\datasets\\city_coordinates.json',
            mode='w', encoding='utf-8') as f:
        f.write(json.dumps(data_new, ensure_ascii=False))  # 将dict转换为str，指定ensure_ascii=False支持中文


if __name__ == '__main__':
    render()