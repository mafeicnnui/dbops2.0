#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/5 12:33
# @Author : ma.fei
# @File : logon.py.py
# @Software: PyCharm

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.locale
from web.utils.urls  import urls
from web.utils.settings import settings

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    print('Dbops2.0 Server running 9000 port ...')
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(9000)
    tornado.ioloop.IOLoop.instance().start()
