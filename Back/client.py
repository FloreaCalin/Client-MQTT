import socket
import threading

from Back.Packet import Connect, Disconnect, PingReq, Publish, Subscribe, Unsubscribe


class Client(object):
    def __init__(self, _id, _username, _password):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def loopGetMessages (self, s):
        while 1:
            message = s.recv (1024)
            if message:
                print (message)

    def connect (self, _host, _port, _keepAlive, _cleanSession, _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain):
        self.__s.connect((_host, _port))

        self.__threadForReceiveMessages = threading.Thread (target = self.loopGetMessages, args = (self.__s,))
        #self.__threadForReceiveMessages.start()

        connPacket = Connect (self.__id, self.__username, self.__password, _keepAlive, _cleanSession,
                              _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain)

        packet = connPacket.makePacket()
        print(packet)
        self.__s.sendall(packet)

        message = self.__s.recv(1024)
        print (message)

    def publish (self, _topicName, _message, _Qos, _dup, _retain):
        publishPacket = Publish(_topicName, _message, _Qos, _dup, _retain)

        packet = publishPacket.makePacket()
        print(packet)
        self.__s.sendall(packet)

        message = self.__s.recv(1024)
        print (message)

    def disconnect (self):
        dissPacket = Disconnect ()

        packet = dissPacket.makePacket()
        self.__s.sendall(packet)

        message = self.__s.recv(1024)
        print (message)

    def pingreq (self):
        pingPacket = PingReq ()

        packet = pingPacket.makePacket()
        self.__s.sendall(packet)

        message = self.__s.recv(1024)
        print (message)

    def subscribe (self, _topicList, _QosList):
        subPacket = Subscribe (_topicList, _QosList)

        packet = subPacket.makePacket()
        self.__s.sendall(packet)
        print (packet)

        message = self.__s.recv(1024)
        print (message)

    def unsubscribe (self, _topicList):
        unSubPacket = Unsubscribe(_topicList)

        packet = unSubPacket.makePacket()

        self.__s.sendall(packet)
        print (packet)

        message = self.__s.recv(1024)
        print (message)