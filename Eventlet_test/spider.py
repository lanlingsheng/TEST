# -*- coding:utf-8 -*-  
__author__ = 'Administrator'


import eventlet
from eventlet.green import urllib2


urls = [
    "http://python.org/images/python-logo.gif",
]


def fetch(url):
    print("opening", url)
    body = urllib2.urlopen(url).read()
    print("done with", url)
    return url, body


pool = eventlet.GreenPool(200)
for url, body in pool.imap(fetch, urls):
    print("got body from", url, "of length", len(body))