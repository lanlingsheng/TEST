# -*- coding:utf-8 -*-  
__author__ = 'Administrator'

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

user = {}


class ChatReci(LineReceiver):
    #定义一个继承自LineReceiver 的类
    def __init__(self):
        self.name = ''
        self.state = "game"

    def connectionMade(self):
        self.sendLine("input you name?")

    def lineReceived(self, data):
        if self.name == '':  # 判断名字书否为空
            self.name = data
            self.sendLine("you welcome, %s" % (self.name))
            user[self.name] = self   # 把用户名和消息赋值给user字典
            print('%s loging' % data)
        else:
            message = "<%s> %s" % (self.name, data)
            for ur, protocol in user.items():
                if protocol != user:
                    protocol.sendLine(message)   # 传送消息


factory = Factory()
factory.protocol = ChatReci
reactor.listenTCP(2222, factory)
reactor.run()
