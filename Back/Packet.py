messageTypes = {
    'CONNECT': b'\x10',
    'CONNACK': b'\x20',
    'PUBLISH': 3,
    'PUBACK': b'\x40',
    'PUBREC': b'\x50',
    'PUBREL': b'\x62',
    'PUBCOMP': b'\x70',
    'SUBSCRIBE': 8,
    'SUBACK': b'\x90',
    'UNSUBSCRIBE': 10,
    'UNSUBACK': b'\xB0',
    'PINGREQ': b'\xC0',
    'PINGRESP': b'\xD0',
    'DISCONNECT': b'\xE0',
}

########################
###  CONNECT ZONE  #####
########################
class Connect(object):
    def __init__(self, _id, _username, _password, _keepAlive, _cleanSession, _lastWillTopic, _lastWillMessage, _lastWillQos, _lastWillRetain):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__keepAlive= _keepAlive
        self.__cleanSession = _cleanSession
        self.__lastWillTopic= _lastWillTopic
        self.__lastWillMessage = _lastWillMessage
        self.__lastWillQos= _lastWillQos
        self.__lastWillRetain = _lastWillRetain

        self.willFlag = None
        if (_lastWillMessage != None):
            self.willFlag = 1

        if (_lastWillQos != None):
            Qo2B0 = (self.__lastWillQos & 1)
            if (Qo2B0 == 0):
                Qo2B0 = None

            Qo2B1 = ((self.__lastWillQos >> 1) & 1)
            if (Qo2B1 == 0):
                Qo2B1 = None
        else:
            Qo2B0 = None
            Qo2B1 = None

        #facem o lista cu valorile ce ar putea aparea in payload, ne ajuta la determinarea flagului
        self.mapConnParam = [_username, _password, _lastWillRetain, Qo2B1, Qo2B0, self.willFlag, _cleanSession, None]

    #scoatem valoarea flagului care indica ce valori avem in payload
    def getFlagValue(self):
        putere = 7
        flagValue = 0
        for value in self.mapConnParam:
            if value != None:
                flagValue = flagValue + 2 ** putere
            putere = putere - 1

        return (flagValue).to_bytes(1, byteorder='big')

    def makePacket (self):
        #Variable header
        variableHeader = b'\x00\x04' #length mqtt string
        variableHeader += ('MQTT').encode ('UTF-8') #protocol name
        variableHeader += b'\x04' #version of mqtt
        variableHeader += self.getFlagValue() #flag
        variableHeader += (self.__keepAlive).to_bytes (2, byteorder='big') #keep alive

        #payload
        #set Id
        payload = (len (str(self.__id))).to_bytes (2, byteorder='big')
        payload += str(self.__id).encode ('UTF-8')

        if (self.willFlag != None):
            payload += (len (self.__lastWillTopic)).to_bytes (2, byteorder='big')
            payload += self.__lastWillTopic.encode ('UTF-8')

            payload += (len (self.__lastWillMessage)).to_bytes (2, byteorder='big')
            payload += self.__lastWillMessage.encode ('UTF-8')

        if (self.__username != None):
            payload += (len (self.__username)).to_bytes (2, byteorder='big')
            payload += self.__username.encode ('UTF-8')


        if (self.__password):
            payload += (len (self.__password)).to_bytes (2, byteorder='big')
            payload += self.__password.encode ('UTF-8')

        stringConcat = variableHeader + payload

        finalPacket = messageTypes['CONNECT']
        finalPacket += len(stringConcat).to_bytes(1, byteorder='big')
        finalPacket += stringConcat
        return finalPacket

class Connack (object):
    def parseData (self, packet):
        response = packet[3]
        if response == 0:
            return 'Connection accepted'
        if response == 1:
            return 'Connection Refused, unacceptable protocol version'
        if response == 2:
            return 'Connection Refused, identifier rejected'
        if response == 3:
            return 'Connection Refused, Server unavailable'
        if response == 4:
            return 'Connection Refused, bad user name or password'
        if response == 5:
            return 'Connection Refused, not authorized'

        return 'Unknown error'

class Disconnect (object):
    def makePacket (self):
        packet = bytearray ()
        packet += messageTypes['DISCONNECT']

        packet += b'\x00'

        return packet



########################
###  PUBLISH ZONE  #####
########################
class Publish (object):
    def __init__ (self, _topicName = '', _message = '', _Qos = 0, _dup = 0, _retain = 0, packetIdentifier = 0):
        self.__topicName = _topicName
        self.__message = _message
        self.__Qos = _Qos
        self.__dup = _dup
        self.__retain = _retain
        self.__packetIdentifier = packetIdentifier

        self.Qo2B0 = (self.__Qos & 1)

        self.Qo2B1 = ((self.__Qos >> 1) & 1)

    def makePacket (self):
        valFixedHeader = messageTypes['PUBLISH'] * 16 + (self.__dup * 8) + (self.Qo2B1 * 4) + (self.Qo2B0 * 2) + (self.__retain * 1)
        finalPacket = valFixedHeader.to_bytes(1, byteorder='big')

        #make variable header
        variableHeader = (len (self.__topicName)).to_bytes(2, byteorder='big')
        variableHeader += (self.__topicName).encode('UTF-8')

        if self.__Qos == 1 or self.__Qos == 2:
            variableHeader += (self.__packetIdentifier).to_bytes(2, byteorder='big')

        payload = (self.__message).encode ('UTF-8')

        stringConcat = variableHeader + payload
        remainingLength = (len(stringConcat)).to_bytes(1, byteorder='big')

        finalPacket += remainingLength + stringConcat

        return finalPacket

    def parseData (self, packet):
        print (packet)
        identifierFirstByte = hex (packet[0])
        identifierSecondByte = hex (packet[1])

        #identify fixed header
        arrayFixedFirstByte = [0, 0, 0, 0]
        putere = 3
        poz = 0
        byte = int(identifierFirstByte[3])
        while (putere >= 0):
            if (byte >= 2 ** putere):
                arrayFixedFirstByte[poz] = 1
                byte -= 2 ** putere
            poz = poz + 1
            putere = putere - 1

        self.__dup = arrayFixedFirstByte[0]
        self.__Qos = (arrayFixedFirstByte[1] << 1) | arrayFixedFirstByte[2]
        self.__retain = arrayFixedFirstByte[3]

        if len (identifierSecondByte) == 4:
            remainingLength = (int(identifierSecondByte[2], 16) << 4) + int (identifierSecondByte[3], 16)
        else:
            remainingLength = int(identifierSecondByte[2], 16)

        #topicLength
        identifier3Byte = hex (packet[2])
        identifier4Byte = hex (packet[3])

        offset = 4
        if (len(identifier3Byte) == 4):
            topicLengthHigh = (int (identifier3Byte[2], 16) << 4) + int (identifier3Byte[3], 16)
        else:
            topicLengthHigh = (int (identifier3Byte[2], 16))

        if (len(identifier4Byte) == 4):
            topicLengthLow = (int (identifier4Byte[2], 16) << 4) + int (identifier4Byte[3], 16)
        else:
            topicLengthLow = (int (identifier4Byte[2], 16))
        topicLength = (topicLengthHigh << 8) + topicLengthLow

        #message and identifier
        topicName = packet[offset : topicLength + offset]

        if (self.__Qos == 1 or self.__Qos == 2):
            identifier3Byte = hex (packet[topicLength + offset])
            identifier4Byte = hex (packet[topicLength + offset + 1])

            if (len(identifier3Byte) == 4):
                packetIdentifierHigh = (int (identifier3Byte[2], 16) << 4) + int (identifier3Byte[3], 16)
            else:
                packetIdentifierHigh = (int (identifier3Byte[2], 16))

            if (len(identifier4Byte) == 4):
                packetIdentifierLow = (int (identifier4Byte[2], 16) << 4) + int (identifier4Byte[3], 16)
            else:
                packetIdentifierLow = (int (identifier4Byte[2], 16))

            packetIdentifier = (packetIdentifierHigh << 8) + packetIdentifierLow
            message = packet[topicLength + offset + 2 : len (packet)]

            return [topicName, message, self.__Qos, packetIdentifier]

        message = packet[topicLength + offset : len (packet)]
        return [topicName, message, self.__Qos, -1]

class Puback (object):
    def makePacket (self, _packetIdentifier):
        packet = bytearray ()
        packet += messageTypes['PUBACK']

        packet += b'\x02'
        packet += _packetIdentifier.to_bytes(2, byteorder='big')

        return packet

    def parseData (self, packet):
        responseHigh = packet[2]
        responseLow = packet[3]

        response = (int(responseHigh) << 8) + int(responseLow)

        return response

class Pubrec (object):
    def makePacket (self, _packetIdentifier):
        packet = bytearray ()
        packet += messageTypes['PUBREC']

        packet += b'\x02'
        packet += _packetIdentifier.to_bytes(2, byteorder='big')

        return packet

    def parseData (self, packet):
        responseHigh = packet[2]
        responseLow = packet[3]

        response = (int(responseHigh) << 8) + int(responseLow)

        return response

class Pubrel (object):
    def makePacket (self, _packetIdentifier):
        packet = bytearray ()
        packet += messageTypes['PUBREL']

        packet += b'\x02'
        packet += _packetIdentifier.to_bytes(2, byteorder='big')

        return packet

    def parseData (self, packet):
        responseHigh = packet[2]
        responseLow = packet[3]

        response = (int(responseHigh) << 8) + int(responseLow)

        return response

class Pubcomp (object):
    def parseData (self, packet):
        responseHigh = packet[2]
        responseLow = packet[3]

        response = (int(responseHigh) << 8) + int(responseLow)

        return response

    def makePacket (self, _packetIdentifier):
        packet = bytearray ()
        packet += messageTypes['PUBCOMP']

        packet += b'\x02'
        packet += _packetIdentifier.to_bytes(2, byteorder='big')

        return packet



########################
###  SUBSCRIBE ZONE ####
########################
class Subscribe (object):
    def __init__ (self, _topicList, _QosList, _packetIdentifier):
        self.__topicList = _topicList
        self.__QosList = _QosList
        self.__packetIdentifier = _packetIdentifier

    def makePacket (self):
        valFixedHeader = messageTypes['SUBSCRIBE'] * 16 + 2
        finalPacket = valFixedHeader.to_bytes(1, byteorder='big')

        variableHeader = self.__packetIdentifier.to_bytes(2, byteorder='big')

        n = len (self.__topicList)
        payload = bytearray ()
        for i in range (0, n):
            payload += (len(self.__topicList[i])).to_bytes(2, byteorder='big')
            payload += (self.__topicList[i]).encode ('UTF-8')

            payload += (self.__QosList[i]).to_bytes(1, byteorder='big')

        stringConcat = variableHeader + payload
        remainingLength = (len(stringConcat)).to_bytes(1, byteorder='big')

        finalPacket += remainingLength + stringConcat

        return finalPacket

class Subpack (object):
    def parseData (self, packet):
        responseHigh = packet[2]
        responseLow = packet[3]

        response = (int(responseHigh) << 8) + int(responseLow)

        return response

class Unsubscribe (object):
    def __init__ (self, _topicList, _packetIdentifier):
        self.__topicList = _topicList
        self.__packetIdentifier = _packetIdentifier

    def makePacket (self):
        valFixedHeader = messageTypes['UNSUBSCRIBE'] * 16 + 2
        finalPacket = valFixedHeader.to_bytes(1, byteorder='big')

        variableHeader = self.__packetIdentifier.to_bytes(2, byteorder='big')

        n = len (self.__topicList)
        payload = bytearray ()
        for i in range (0, n):
            payload += (len(self.__topicList[i])).to_bytes(2, byteorder='big')
            payload += (self.__topicList[i]).encode ('UTF-8')

        stringConcat = variableHeader + payload
        remainingLength = (len(stringConcat)).to_bytes(1, byteorder='big')

        finalPacket += remainingLength + stringConcat

        return finalPacket

class Unsuback (object):
    def parseData (self, packet):
        responseHigh = packet[2]
        responseLow = packet[3]

        response = (int(responseHigh) << 8) + int(responseLow)

        return response



########################
#####  PING ZONE  ######
########################
class PingReq (object):
    def makePacket (self):
        packet = bytearray ()
        packet += messageTypes['PINGREQ']

        packet += b'\x00'

        return packet

class Pingresp (object):
    def parseData (self, packet):
        return 'Pingresp'