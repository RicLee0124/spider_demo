#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 18:22
# @Author  : RicLee
# @Site    : 
# @File    : Test.py
# @Software: PyCharm

import time

tm = time.strptime('2018-08-13 09:43:11', '%Y-%m-%d %H:%M:%S')
print(tm.tm_hour)
