#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 14:52
# @Author  : RicLee
# @Site    : 
# @File    : DataClean.py
# @Software: PyCharm

import pymysql
import csv


def getData():
    with open("C:\\Users\\lichao\\Desktop\\财经\\财经19.csv", "r", encoding="utf-8") as csvfile:
        # 读取csv文件，返回的是迭代类型
        data = csv.reader(csvfile)
        for row in data:
            print(len(row))
            domain = row[0]
            title = row[1]
            link = row[2]
            createdate = row[3]
            author = row[4]
            zddz = row[5]
            zwdz = row[6]
            zfm = row[7]
            zzs = row[8]
            hfs = row[9]
            djl = row[10]
            piclink = row[11]
            sfljxx = row[12]
            content = row[12:]
            print(domain,title,"----------",link,"--------",createdate,author,zddz,zwdz,zfm,zzs,hfs,djl,"--------",piclink,"--------",sfljxx,content)


# 存储数据到MySQL
def save_to_mysql(data):
    config = {
        'host': '10.1.12.188',
        'port': 3306,
        'user': 'root',
        'password': '1234@abcd',
        'database': 'test',
        'charset': 'utf8'
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = '''
        insert into t_job
          (title, company, addr, salary, pubDate) 
        values 
          (%(title)s,%(company)s,%(addr)s,%(salary)s,%(pubDate)s)  
    '''
    cursor.executemany(sql, data)
    conn.commit()

    cursor.close()
    conn.close()



if __name__ == '__main__':
    getData()
