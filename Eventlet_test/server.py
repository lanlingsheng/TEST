# -*- coding:utf-8 -*-  
#__author__ = 'Administrator'

from __future__ import print_function

import eventlet


def handle(fd):
    # 单个协程的处理器
    print('clientd connected')
    while True:
        # pass through every non-eof line
        x = fd.readline()
        if not x:
            break
        fd.write(x)
        fd.flush()
        print("echoed", x, end=' ')
    print("client disconnected")


print("server socket listening on port 6000")
server = eventlet.listen(('0.0.0.0', 6000))
#监听 6000 端口
pool = eventlet.GreenPool()
# 构造协程池
while True:
    try:
        new_sock, address = server.accept()
        # accept 新的连接
        print("accepted", address)
        pool.spawn(handle, new_sock.makefile('rw'))
        # 将新的连接交由一个新的协程去处理
    except (SystemExit, KeyboardInterrupt):
        break