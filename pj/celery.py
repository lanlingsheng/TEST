# -*- coding:utf-8 -*-  
#__author__ = 'Administrator'


from __future__ import absolute_import
from celery import Celery


app = Celery('pj',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['pj.tasks'])


app.config_from_object('pj.config')


if __name__ == '__main__':
    app.start()