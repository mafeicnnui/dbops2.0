#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/5 12:50
# @Author : ma.fei
# @File : common.py.py
# @Software: PyCharm


import json
import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)
