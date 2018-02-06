# -*- coding:utf-8 -*-  
__author__ = 'Administrator'


import eventlet
from eventlet.green import socket

PORT = 3001
particiants = set()


def read_chat_forever(writer, reader):
    line = reader.readline()
    while line:
        print("Chat: ", line.strip())
        for p in particiants:
            try:
                if p is not writer:
                    p.write(line)
                    p.flush()
            except socket.error as e:
                if e[0] != 32:
                    raise
        line = reader.readline()
    particiants.remove(writer)
    print("Participant left chat.")


try:
    print("ChatServer starting up on port %s"% PORT)
    server = eventlet.listen(('0.0.0.0', PORT))
    while True:
        new_connection, address = server.accept()
        print("Participant joined chat.")
        new_writer = new_connection.makefile('w')
        particiants.add(new_writer)
        eventlet.spawn_n(read_chat_forever, new_writer, new_connection.makefile('r'))
except (KeyboardInterrupt, SystemExit):
    print("ChatServer exiting.")
