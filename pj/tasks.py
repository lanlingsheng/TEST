# -*- coding:utf-8 -*-  
__author__ = 'Administrator'


#from __future__ import absolute_import

from celery import Celery
from celery import group

from pj.celery import app


#app = Celery('tasks', broker='redis://127.0.0.1:6379/5')


@app.task
def add(x, y):
    return x + y

@app.task
def subtract(x, y):
    return x - y