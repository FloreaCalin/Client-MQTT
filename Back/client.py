import socket
import threading
import time

from Back.Packet import Connect, Disconnect, PingReq, Publish, Subscribe, Unsubscribe

class Client(object):
    __queueMessages = []
    __keepAliveMaxTime = 0
    def __init__(self, _id, _username, _password):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__keepAliveCounter = 0
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def loopGetMessages (self, s):
        while 1:
            message = s.recv (2048)
            if message:
                self.__queueMessages.append(message)

    def loopHandleQueue (self):
        while 1:
            while (self.__queueMessages):
                print (self.__queueMessages[0])
                self.__queueMessages.pop(0)

    def keepAliveCount (self):
        while 1:
            time.sleep (1)
            self.__keepAliveCounter += 1
            if (self.__keepAliveCounter >= self.__keepAliveMaxTime):
                self.__sendPing()

    def __sendPing (self):
        self.pingreq()
        self.__keepAliveCounter = 0

    def connect (self, _host, _port, _keepAlive, _cleanSession, _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain):
        self.__s.connect((_host, _port))
        self.__keepAliveMaxTime = _keepAlive

        self.__threadForReceiveMessages = threading.Thread (target = self.loopGetMessages, args = (self.__s,))
        #self.__threadForReceiveMessages.start()

        self.__threadForHandleMessages = threading.Thread (target = self.loopHandleQueue, args = ())
        self.__threadForHandleMessages.start()

        self.__threadForKeepAliveCounter = threading.Thread (target = self.keepAliveCount, args = ())
        self.__threadForKeepAliveCounter.start()

        connPacket = Connect (self.__id, self.__username, self.__password, _keepAlive, _cleanSession,
                              _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain)

        packet = connPacket.makePacket()
        self.__s.sendall(packet)
        self.__keepAliveCounter = 0 #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def publish (self, _topicName, _message, _Qos, _dup, _retain):
        publishPacket = Publish(_topicName, _message, _Qos, _dup, _retain)

        packet = publishPacket.makePacket()
        #print(packet)
        self.__s.sendall(packet)
        self.__keepAliveCounter = 0 #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def disconnect (self):
        dissPacket = Disconnect ()

        packet = dissPacket.makePacket()
        self.__s.sendall(packet)
        self.__keepAliveCounter = 0 #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def pingreq (self):
        pingPacket = PingReq ()

        packet = pingPacket.makePacket()
        self.__s.sendall(packet)
        self.__keepAliveCounter = 0 #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def subscribe (self, _topicList, _QosList):
        subPacket = Subscribe (_topicList, _QosList)

        packet = subPacket.makePacket()
        self.__s.sendall(packet)
        self.__keepAliveCounter = 0 #send message, reset keep alive time
        #print (packet)

        #message = self.__s.recv(1024)
        #print (message)

    def unsubscribe (self, _topicList):
        unSubPacket = Unsubscribe(_topicList)

        packet = unSubPacket.makePacket()

        self.__s.sendall(packet)
        self.__keepAliveCounter = 0 #send message, reset keep alive time
        #print (packet)

        #message = self.__s.recv(1024)
        #print (message)