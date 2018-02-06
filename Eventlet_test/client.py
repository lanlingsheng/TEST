# -*- coding:utf-8 -*-  
#__author__ = 'Administrator'


from __future__ import print_function
import eventlet
from eventlet.green import urllib2


def myfetch(myurl, i):
    req = urllib2.Request(myurl)
    req.add_header('User-agent', 'Mozilla 5.10')
    res = urllib2.urlopen(req, timeout=4)
    body = res.read()
    size = len(body)
    print(i, 'body size', size)
    return size


myurl = "http://127.0.0.1:6000"
pool = eventlet.GreenPool(1000)
for i in range(1, 200):
    pool.spawn(myfetch, myurl, i)
    print(i)
pool.waitall()
print("--finish --GreenPool")