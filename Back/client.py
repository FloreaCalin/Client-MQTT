import socket
import threading
import time

from Back.Packet import Connect, Disconnect, PingReq, Publish, Subscribe, Unsubscribe, Pubrel, Connack, Puback, Pubrec, \
    Pubcomp, Subpack, Unsuback, Pingresp

listOfMessages = []
connectResponse = ''

def getConnectResponse ():
    return connectResponse

class Client(object):
    #init data
    __queueMessages = []
    __keepAliveMaxTime = 0
    def __init__(self, _id, _username, _password):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__keepAliveCounter = 0
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__packetIdentifier = 0

    #threads for get, interpret, messages and handle keep alive
    def loopGetMessages (self, s):
        while 1:
            message = s.recv (1024)
            if message:
                self.__queueMessages.append(message)

    def loopHandleQueue (self):
        while 1:
            while (self.__queueMessages):
                self.__identifyPacket(self.__queueMessages[0])
                self.__queueMessages.pop(0)

    def __identifyPacket (self, packet):
        identifierFirstByte = hex (packet[0])
        identifierSecondByte = hex (packet[1])

        if identifierFirstByte == '0x20' and identifierSecondByte == '0x2': #connack
            connackPacket = Connack ()
            response = connackPacket.parseData(packet)
            connectResponse = response
            print (response)

        elif identifierFirstByte[2] == '3': #publish back
            publishPacket = Publish ()
            response = publishPacket.parseData(packet)

            #test QOS
            if (response[2] == 0): #QOS = 0
                topic = str (response[0])
                message = str (response[1])
                listOfMessages.append ('topic: ' + topic[2 : len (topic) - 1] + '\nmessage: ' + message[2 : len (message) - 1])

            if (response[2] == 1): #QOS = 1
                pubackPacket = Puback ()
                packetToSend = pubackPacket.makePacket(response[3])

                topic = str (response[0])
                message = str (response[1])
                listOfMessages.append('topic: ' + topic[2 : len (topic) - 1] + '\nmessage: ' + message[2 : len (message) - 1])

                self.__s.sendall(packetToSend)
                self.resetKeepAlive()

            if (response[2] == 2): #QOS = 2
                pubrecPacket = Pubrec ()
                packetToSend = pubrecPacket.makePacket(response[3])

                topic = str (response[0])
                message = str (response[1])
                listOfMessages.append ('topic: ' + topic[2 : len (topic) - 1] + '\nmessage: ' + message[2 : len (message) - 1])
                print ("send pubrec for: " + str (response[3]))
                self.__s.sendall(packetToSend)
                self.resetKeepAlive()

        elif identifierFirstByte == '0x40' and identifierSecondByte == '0x2': #puback
            pubackPacket = Puback ()
            responseID = pubackPacket.parseData(packet)

            print ("Mesaj trimis cu succes QoS1 cu id ul: " + str(responseID))

        elif identifierFirstByte == '0x50' and identifierSecondByte == '0x2': #pubrec
            pubrecPacket = Pubrec ()
            responseID = pubrecPacket.parseData(packet)

            pubrelPacket = Pubrel ()
            packetToSend = pubrelPacket.makePacket(responseID)

            self.__s.sendall(packetToSend)
            self.resetKeepAlive()

        elif identifierFirstByte == '0x62' and identifierSecondByte == '0x2': #pubrel
            pubrelPacket = Pubrel ()
            responseID = pubrelPacket.parseData(packet)

            pubcompPacket = Pubcomp ()
            packetToSend = pubcompPacket.makePacket(responseID)

            print ("send pubcomp for: " + str (responseID))
            self.__s.sendall(packetToSend)
            self.resetKeepAlive()

        elif identifierFirstByte == '0x70' and identifierSecondByte == '0x2': #pubcomp
            pubcompPacket = Pubcomp ()
            responseID = pubcompPacket.parseData(packet)

            print ("Mesaj trimis cu succes QoS2 cu id ul: " + str(responseID))

        elif identifierFirstByte == '0x90': #subpack
            subpackPacket = Subpack ()
            responseID = subpackPacket.parseData(packet)

            print ("Subscribe cu succes la id ul: " + str (responseID))

        elif identifierFirstByte == '0xb0': #unsuback
            unsubackPacket = Unsuback ()
            responseID = unsubackPacket.parseData(packet)

            print ("Unsubscribe la id ul:" + str (responseID))

        elif (identifierFirstByte == '0xd0'):
            pingrespPacket = Pingresp ()

            response = pingrespPacket.parseData(packet)

            print (response)

    def keepAliveCount (self):
        while 1:
            time.sleep (1)
            self.__keepAliveCounter += 1
            if (self.__keepAliveCounter >= self.__keepAliveMaxTime):
                self.__sendPing()

    def __sendPing (self):
        self.pingreq()
        self.__keepAliveCounter = 0

    #functions to make operations to server
    def connect (self, _host, _port, _keepAlive, _cleanSession, _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain):
        self.__s.connect((_host, _port))
        self.__keepAliveMaxTime = _keepAlive

        self.__threadForReceiveMessages = threading.Thread (target = self.loopGetMessages, args = (self.__s,))
        self.__threadForReceiveMessages.start()

        self.__threadForHandleMessages = threading.Thread (target = self.loopHandleQueue, args = ())
        self.__threadForHandleMessages.start()

        self.__threadForKeepAliveCounter = threading.Thread (target = self.keepAliveCount, args = ())
        self.__threadForKeepAliveCounter.start()

        connPacket = Connect (self.__id, self.__username, self.__password, _keepAlive, _cleanSession,
                              _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain)

        packet = connPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive() #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def publish (self, _topicName, _message, _Qos, _dup, _retain):
        self.__packetIdentifier += 1 #increase packet identidier
        publishPacket = Publish(_topicName, _message, _Qos, _dup, _retain, self.__packetIdentifier)

        packet = publishPacket.makePacket()
        #print(packet)
        self.__s.sendall(packet)
        self.resetKeepAlive() #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def disconnect (self):
        self.__packetIdentifier += 1 #increase packet identidier
        dissPacket = Disconnect ()

        packet = dissPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive() #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def pingreq (self):
        pingPacket = PingReq ()

        packet = pingPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive() #send message, reset keep alive time

        #message = self.__s.recv(1024)
        #print (message)

    def subscribe (self, _topicList, _QosList):
        self.__packetIdentifier += 1 #increase packet identidier
        subPacket = Subscribe (_topicList, _QosList, self.__packetIdentifier)

        packet = subPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive() #send message, reset keep alive time
        #print (packet)

        #message = self.__s.recv(1024)
        #print (message)

    def unsubscribe (self, _topicList):
        self.__packetIdentifier += 1 #increase packet identidier
        unSubPacket = Unsubscribe(_topicList, self.__packetIdentifier)

        packet = unSubPacket.makePacket()

        self.__s.sendall(packet)
        self.resetKeepAlive() #send message, reset keep alive time
        #print (packet)

        #message = self.__s.recv(1024)
        #print (message)

    def resetKeepAlive (self):
        self.__keepAliveCounter = 0

