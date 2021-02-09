#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/5 12:33
# @Author : ma.fei
# @File : logon.py.py
# @Software: PyCharm

import tornado.web
from web.model.t_user import T_user
from web.utils.peewee import database

class users(tornado.web.RequestHandler):
    def get(self,type):
        if type == 'all':
            with database:
                users = T_user.select()
            self.render("user_query2.html",user=users)
        else:
            with database:
                user = T_user.get(id=type)
            self.render("user_query.html", user=user)

    def post(self,type):
        if type == 'create':
            with database:
                user = T_user.create(name='马飞',
                                   wkno='190343',
                                   gender='1',
                                   email='190343@lifeat.cn',
                                   phone='12343434343',
                                   dept='2',
                                   expire_date='2020-12-31',
                                   password='Abcd@1234',
                                   status='1',
                                   creator='dba',
                                   updator='dba',
                                   login_name='mafei')
            self.write('user {} insert success!'.format(user.id))

        if type == 'update':
            with database:
                user = T_user.get(id=4)
                user.name        = '张飞'
                user.wkno        = '190348'
                user.gender      = '1'
                user.email       = '190243@lifeat.cn'
                user.phone       = '12343434363'
                user.dept        = '2'
                user.expire_date = '2020-12-31'
                user.password    = 'Abcd@1234'
                user.status      = '1'
                user.creator     = 'ocm'
                user.updator     = 'ocm'
                user.last_update_date = '2021-02-05'
                user.login_name  = 'zhang.fei'
                user.save()
            self.write('user {} update success!'.format(user.id))



