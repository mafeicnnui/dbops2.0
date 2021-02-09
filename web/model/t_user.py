#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/5 9:49
# @Author : ma.fei
# @File : t_user.py.py
# @Software: PyCharm

import warnings
import datetime
from peewee import *
from web.utils.peewee import BaseModel,database
warnings.filterwarnings("ignore")

class T_user(BaseModel):
    name               = CharField(max_length=20)
    wkno               = CharField(max_length=20)
    gender             = CharField(max_length=2)
    email              = CharField(max_length=40)
    phone              = CharField(max_length=20)
    dept               = CharField(max_length=20)
    expire_date        = DateField(default=datetime.datetime.now)
    password           = CharField(max_length=200)
    status             = CharField(max_length=1)
    login_name         = CharField(max_length=20)
    class Meta:
        table_name = 't_user'

if __name__=='__main__':
    with database:
        print('drop table...')
        database.drop_tables([T_user])
        print('create table ...')
        database.create_tables([T_user])


