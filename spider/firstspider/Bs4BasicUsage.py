#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 16:56
# @Author  : RicLee
# @Site    : 
# @File    : Bs4BasicUsage.py
# @Software: PyCharm


from bs4 import BeautifulSoup

def getBs():
    with open('test.html', mode='r', encoding='gbk') as f:
        html = f.read()

    #  创建BeautifulSoup实例，解析html数据
    bs = BeautifulSoup(html, 'html.parser')  # 指定使用html解析器parser
    return bs

#根据标签来获取
def demo1():
    bs = getBs()
    #1.find()方法，获取第一个匹配的标签
    div = bs.findAll('div')
    print(div)

#根据id或class来获取
def demo2():
    bs = getBs()
    divs1 = bs.find(id='div2')
    print(divs1)
    divs2 = bs.find(class_='div4')
    print(divs2)

# 3.select()方法，使用CSS选择器来获取元素
def demo3():
    bs = getBs()
    print(bs.select('.div1')) #查找class=div1的元素
    print(bs.select('#div2')) #查找id=div2的元素
    print(bs.select('.div1 #div2 p')) #查找class=div1 id=div2 下的p标签


# 获取文本
def demo4():
    bs = getBs()
    value = bs.select('.div1')[0].get_text(strip=True)
    print(value)


if __name__ == '__main__':
    demo4()
