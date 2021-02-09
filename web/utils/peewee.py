#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/5 10:27
# @Author : ma.fei
# @File : peewee.py.py
# @Software: PyCharm

import datetime
from peewee import *

config =  {
        "host"     : "10.2.39.17",
        "user"     : "puppet",
        "passwd"   : "Puppet@123",
        "database" : "puppet2.0",
        "port"     :  23306
}

database = MySQLDatabase(**config)

class BaseModel(Model):
    creator          = CharField(max_length=20)
    updator          = CharField(max_length=20)
    creation_date    = DateTimeField(default=datetime.datetime.now)
    last_update_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

