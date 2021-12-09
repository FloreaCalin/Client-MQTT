import socket

from Back.Packet import Connect, Disconnect, PingReq, Publish


class Client(object):
    def __init__(self, _id, _username, _password):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect (self, _host, _port, _keepAlive, _cleanSession, _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain):
        self.__s.connect((_host, _port))

        connPacket = Connect (self.__id, self.__username, self.__password, _keepAlive, _cleanSession,
                              _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain)

        packet = connPacket.makePacket()
        print(packet)
        self.__s.sendall(packet)

        message = self.__s.recv(1024)
        print (message)

    def publish (self, _topicName, _message, _Qos, _packetIdentifier):
        publishPacket = Publish(_topicName, _message, _Qos, _packetIdentifier)

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