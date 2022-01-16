import time

from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('broker.mqttdashboard.com', 1883, 5, 1, "Last Will", "E DE JALE!", 1, 1)
    #client.pingreq()

    #client.publish('topic/something', "message", 0, 0, 0)
    #client.publish('topic/something/ceva', "mesajJMECKER", 0, 0, 0)
    client.publish('topic/something/inca/ceva', "!mesajSiMaiJmecker", 0, 0, 0)
    client.subscribe(['testtopic/#'], [0])

    #client.unsubscribe(['topic/#'])
    #client.disconnect()
