#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/5 9:49
# @Author : ma.fei
# @File : mysql.py.py
# @Software: PyCharm

import pymysql
from   web.utils.settings import settings

def get_db(p_type = None):
    if p_type is None:
        return pymysql.connect(**settings['db'])
    elif p_type == 'dict':
        return pymysql.connect(**settings['db'],cursorclass=pymysql.cursors.DictCursor)
    else:
        raise  Exception("p_type is invalid!")


class mysql_processer:
    def __init__(self,p_type):
        self.type = p_type

    def __enter__(self):
        self.db = get_db(self.type)
        self.cr = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


if __name__=='__main__':
    # test dict format
    with mysql_processer('dict') as m:
         m.cr.execute('select * from t_user')
         rs = m.cr.fetchall()
         for i in rs:
            print(i)

    # test touple format
    with mysql_processer(None) as m:
        m.cr.execute('select * from t_user')
        rs = m.cr.fetchall()
        for i in rs:
            print(i)

    # test exception
    with mysql_processer('xxx') as m:
        m.cr.execute('select * from t_user')
        rs = m.cr.fetchall()
        for i in rs:
            print(i)
