import socket
import threading
import time
from datetime import datetime

from Back.Packet import Connect, Disconnect, PingReq, Publish, Subscribe, Unsubscribe, Pubrel, Connack, Puback, Pubrec, \
    Pubcomp, Subpack, Unsuback, Pingresp

#data for front interface
listOfMessages = []

flagChangeSubscribeList = False
listOfSubscribes = [[], []]

flagConnectResponse = False
connectResponse = ''

#maps for handle response from server
mapForReceivedMessagesQOS2 = {}
mapForPublishQ0SBig = {}
mapForSubscribe = {}
mapForUnsubscribe = {}

#send data to front-end
def getlistOfSubscribes():
    listforReturn = [[], []]
    listforReturn[0] = listOfSubscribes[0].copy()
    listforReturn[1] = listOfSubscribes[1].copy()

    return listforReturn

def getConnectResponse():
    return connectResponse

#handle flags for front end
def getFlagChangeSubscribeList():
    return flagChangeSubscribeList

def setFlagChangeSubscribeList(flagNewValue):
    flagChangeSubscribeList = flagNewValue

def getFlagConnectResponse():
    return flagConnectResponse

def setFlagConnectResponse(flagNewValue):
    flagConnectResponse = flagNewValue

class Client(object):
    # init data
    __queueMessages = []
    __keepAliveMaxTime = 0

    def __init__(self, _id, _username, _password):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__keepAliveCounter = 0
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__packetIdentifier = 0

    # threads for get, interpret, messages and handle keep alive
    def loopGetMessages(self, s):
        while 1:
            message = s.recv(2048)
            if message:
                self.__queueMessages.append(message)

    def loopHandleQueue(self):
        while 1:
            while (self.__queueMessages):
                self.__identifyPacket(self.__queueMessages[0])
                self.__queueMessages.pop(0)

    def looHandleMessagesreceivedQOS2(self):
        while 1:
            FMT = '%H:%M:%S'
            now = datetime.now()
            current_time = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

            if len(list(mapForReceivedMessagesQOS2.keys())) > 0:
                firstElement = list(mapForReceivedMessagesQOS2.keys())[0]
                currentElement = mapForReceivedMessagesQOS2[firstElement]
                tdelta = datetime.strptime(current_time, FMT) - datetime.strptime(currentElement[1], FMT)
                if tdelta.total_seconds() >= self.__keepAliveMaxTime:
                    mapForReceivedMessagesQOS2.pop(firstElement)

    def loopHandleForPublishQ0SBig(self):
        while 1:
            FMT = '%H:%M:%S'
            now = datetime.now()
            current_time = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

            if len(list(mapForPublishQ0SBig.keys())) > 0:
                firstElement = list(mapForPublishQ0SBig.keys())[0]
                currentElement = mapForPublishQ0SBig[firstElement]
                tdelta = datetime.strptime(current_time, FMT) - datetime.strptime(currentElement[1], FMT)
                if tdelta.total_seconds() >= self.__keepAliveMaxTime:
                    if currentElement[4] == 1:
                        mapForPublishQ0SBig.pop(firstElement)
                    else:
                        packetToSend = Publish(currentElement[2], currentElement[0], currentElement[3], 1,
                                               currentElement[5], currentElement[6]).makePacket()
                        self.__s.sendall(packetToSend)
                        mapForPublishQ0SBig.pop(firstElement)
                        mapForPublishQ0SBig[currentElement[6]] = [currentElement[0], currentElement[1],
                                                                  currentElement[2], currentElement[3],
                                                                  1, currentElement[5], currentElement[6]]

    def loopforSubscribe(self):
        while 1:
            FMT = '%H:%M:%S'
            now = datetime.now()
            current_time = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

            if len(list(mapForSubscribe.keys())) > 0:
                firstElement = list(mapForSubscribe.keys())[0]
                currentElement = mapForSubscribe[firstElement]
                tdelta = datetime.strptime(current_time, FMT) - datetime.strptime(currentElement[2], FMT)
                if tdelta.total_seconds() >= self.__keepAliveMaxTime:
                    mapForSubscribe.pop(firstElement)

    def loopforUnsubscribe(self):
        while 1:
            FMT = '%H:%M:%S'
            now = datetime.now()
            current_time = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

            if len(list(mapForUnsubscribe.keys())) > 0:
                firstElement = list(mapForUnsubscribe.keys())[0]
                currentElement = mapForUnsubscribe[firstElement]
                tdelta = datetime.strptime(current_time, FMT) - datetime.strptime(currentElement[1], FMT)
                if tdelta.total_seconds() >= self.__keepAliveMaxTime:
                    mapForUnsubscribe.pop(firstElement)

    def __identifyPacket(self, packet):
        identifierFirstByte = hex(packet[0])
        identifierSecondByte = hex(packet[1])

        if identifierFirstByte == '0x20' and identifierSecondByte == '0x2':  # connack
            connackPacket = Connack()
            response = connackPacket.parseData(packet)
            connectResponse = response
            setFlagConnectResponse(True)

        elif identifierFirstByte[2] == '3':  # publish back
            publishPacket = Publish()
            response = publishPacket.parseData(packet)

            # test QOS
            if (response[2] == 0):  # QOS = 0
                topic = str(response[0])
                message = str(response[1])
                listOfMessages.append(
                    'topic: ' + topic[2: len(topic) - 1] + '\nmessage: ' + message[2: len(message) - 1])

            if (response[2] == 1):  # QOS = 1
                pubackPacket = Puback()
                packetToSend = pubackPacket.makePacket(response[3])

                topic = str(response[0])
                message = str(response[1])
                listOfMessages.append(
                    'topic: ' + topic[2: len(topic) - 1] + '\nmessage: ' + message[2: len(message) - 1])

                self.__s.sendall(packetToSend)
                self.resetKeepAlive()

            if (response[2] == 2):  # QOS = 2
                pubrecPacket = Pubrec()
                packetToSend = pubrecPacket.makePacket(response[3])

                topic = str(response[0])
                message = str(response[1])
                messageToSent = 'topic: ' + topic[2: len(topic) - 1] + '\nmessage: ' + message[2: len(message) - 1]
                now = datetime.now()
                FMT = '%H:%M:%S'
                current_timeReceive = now.strftime(FMT)

                mapForReceivedMessagesQOS2[response[3]] = [messageToSent, current_timeReceive]
                self.__s.sendall(packetToSend)
                self.resetKeepAlive()

        elif identifierFirstByte == '0x40' and identifierSecondByte == '0x2':  # puback
            pubackPacket = Puback()
            responseID = pubackPacket.parseData(packet)

            mapForPublishQ0SBig.pop(responseID)
            print("Mesaj trimis cu succes QoS1 cu id ul: " + str(responseID))

        elif identifierFirstByte == '0x50' and identifierSecondByte == '0x2':  # pubrec
            pubrecPacket = Pubrec()
            responseID = pubrecPacket.parseData(packet)

            pubrelPacket = Pubrel()
            packetToSend = pubrelPacket.makePacket(responseID)

            self.__s.sendall(packetToSend)
            self.resetKeepAlive()

        elif identifierFirstByte == '0x62' and identifierSecondByte == '0x2':  # pubrel
            pubrelPacket = Pubrel()
            responseID = pubrelPacket.parseData(packet)

            pubcompPacket = Pubcomp()
            packetToSend = pubcompPacket.makePacket(responseID)

            listOfMessages.append(mapForReceivedMessagesQOS2[responseID][0])
            mapForReceivedMessagesQOS2.pop(responseID)


            self.__s.sendall(packetToSend)
            self.resetKeepAlive()

        elif identifierFirstByte == '0x70' and identifierSecondByte == '0x2':  # pubcomp
            pubcompPacket = Pubcomp()
            responseID = pubcompPacket.parseData(packet)

            mapForPublishQ0SBig.pop(responseID)
            print("Mesaj trimis cu succes QoS2 cu id ul: " + str(responseID))

        elif identifierFirstByte == '0x90':  # subpack
            subpackPacket = Subpack()
            responseID = subpackPacket.parseData(packet)

            length = len(mapForSubscribe[responseID][0])

            for i in range(0, length):
                listOfSubscribes[0].append(mapForSubscribe[responseID][0][i])
                listOfSubscribes[1].append(mapForSubscribe[responseID][1][i])
            mapForSubscribe.pop(responseID)

            setFlagChangeSubscribeList(True)
            print("Subscribe cu succes la id ul: " + str(responseID))

        elif identifierFirstByte == '0xb0':  # unsuback
            unsubackPacket = Unsuback()
            responseID = unsubackPacket.parseData(packet)

            length = len(listOfSubscribes[0])
            listForDelete = []

            for i in range(0, length):
                lenthMap = len (mapForUnsubscribe[responseID][0])
                for j in range(0, lenthMap):
                    if listOfSubscribes[0][i] == mapForUnsubscribe[responseID][0][j]:
                        listForDelete.append(i)

            listForDeleteFinal = set(listForDelete)

            for element in listForDeleteFinal:
                listOfSubscribes[0].pop(element)
                listOfSubscribes[1].pop(element)

            setFlagChangeSubscribeList(True)
            print("Unsubscribe la id ul:" + str(responseID))

        elif identifierFirstByte == '0xd0':
            pingrespPacket = Pingresp()

            response = pingrespPacket.parseData(packet)

            print(response)

    def keepAliveCount(self):
        while 1:
            time.sleep(1)
            self.__keepAliveCounter += 1
            if self.__keepAliveCounter >= self.__keepAliveMaxTime:
                self.__sendPing()

    def __sendPing(self):
        self.pingreq()
        self.__keepAliveCounter = 0

    # functions to make operations to server
    def connect(self, _host, _port, _keepAlive, _cleanSession, _lastWillTopic, _lastWillMessage, _lastWillQos,
                _lastWillRetain):
        self.__s.connect((_host, _port))
        self.__keepAliveMaxTime = _keepAlive

        self.__threadForReceiveMessages = threading.Thread(target=self.loopGetMessages, args=(self.__s,))
        self.__threadForReceiveMessages.start()

        self.__threadForHandleMessages = threading.Thread(target=self.loopHandleQueue, args=())
        self.__threadForHandleMessages.start()

        self.__threadForKeepAliveCounter = threading.Thread(target=self.keepAliveCount, args=())
        self.__threadForKeepAliveCounter.start()

        self.__threadForHandleMessagesreceivedQOS2 = threading.Thread(target=self.looHandleMessagesreceivedQOS2,
                                                                      args=())
        self.__threadForHandleMessagesreceivedQOS2.start()

        self.__threadHandleForPublishQ0SBig = threading.Thread(target=self.loopHandleForPublishQ0SBig,
                                                               args=())
        self.__threadHandleForPublishQ0SBig.start()

        self.__threadForHandleSubscribe = threading.Thread(target=self.loopforSubscribe, args=())
        self.__threadForHandleSubscribe.start()

        self.__threadForHandleUnsubscribe = threading.Thread(target=self.loopforUnsubscribe, args=())
        self.__threadForHandleUnsubscribe.start()

        connPacket = Connect(self.__id, self.__username, self.__password, _keepAlive, _cleanSession,
                             _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain)

        packet = connPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive()  # send message, reset keep alive time

        # message = self.__s.recv(1024)
        # print (message)

    def publish(self, _topicName, _message, _Qos, _dup, _retain):
        self.increasePacketIdentifier()  # increase packet identidier
        publishPacket = Publish(_topicName, _message, _Qos, _dup, _retain, self.__packetIdentifier)

        packet = publishPacket.makePacket()
        # print(packet)
        self.__s.sendall(packet)

        if (_Qos == 1 or _Qos == 2):
            now = datetime.now()
            FMT = '%H:%M:%S'
            current_timeSend = now.strftime(FMT)
            mapForPublishQ0SBig[self.__packetIdentifier] = [_message, current_timeSend, _topicName, _Qos, _dup, _retain,
                                                            self.__packetIdentifier]

        self.resetKeepAlive()  # send message, reset keep alive time

        # message = self.__s.recv(1024)
        # print (message)

    def disconnect(self):
        self.increasePacketIdentifier()  # increase packet identidier
        dissPacket = Disconnect()

        packet = dissPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive()  # send message, reset keep alive time

        # message = self.__s.recv(1024)
        # print (message)

    def pingreq(self):
        pingPacket = PingReq()

        packet = pingPacket.makePacket()
        self.__s.sendall(packet)
        self.resetKeepAlive()  # send message, reset keep alive time

        # message = self.__s.recv(1024)
        # print (message)

    def subscribe(self, _topicList, _QosList):
        self.increasePacketIdentifier()  # increase packet identidier
        subPacket = Subscribe(_topicList, _QosList, self.__packetIdentifier)

        packet = subPacket.makePacket()
        self.__s.sendall(packet)

        # save subscribe on map to wait for response
        now = datetime.now()
        FMT = '%H:%M:%S'
        current_timeSend = now.strftime(FMT)
        mapForSubscribe[self.__packetIdentifier] = [_topicList, _QosList, current_timeSend]

        self.resetKeepAlive()  # send message, reset keep alive time
        # print (packet)

        # message = self.__s.recv(1024)
        # print (message)

    def unsubscribe(self, _topicList):
        self.increasePacketIdentifier()  # increase packet identidier
        unSubPacket = Unsubscribe(_topicList, self.__packetIdentifier)

        packet = unSubPacket.makePacket()

        # save unsubscribe on map to wait for response
        now = datetime.now()
        FMT = '%H:%M:%S'
        current_timeSend = now.strftime(FMT)
        mapForUnsubscribe[self.__packetIdentifier] = [_topicList, current_timeSend]

        self.__s.sendall(packet)
        self.resetKeepAlive()  # send message, reset keep alive time
        # print (packet)

        # message = self.__s.recv(1024)
        # print (message)

    def resetKeepAlive(self):
        self.__keepAliveCounter = 0

    def increasePacketIdentifier(self):
        if self.__packetIdentifier == (1 << 16) - 1:
            self.__packetIdentifier = 0
        self.__packetIdentifier += 1
