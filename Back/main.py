import time

from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('broker.mqttdashboard.com', 1883, 100, 1, "Last Will", "E DE JALE!", 1, 1)

    #client.publish('topic/something', "message", 0, 0, 0)
    client.subscribe(['topic/something/inca/ceva/#'], [0])
    time.sleep(3)
    client.publish('topic/something/inca/ceva/1234', "mesajJMECKER", 0, 0, 0)
    time.sleep(1)
    client.publish('topic/something/inca/ceva', "mesajSiMaiJmeckerQOs1", 1, 0, 0)
    time.sleep(1)
    client.publish('topic/something/inca/ceva', "mesajSiMaiJmecker", 2, 0, 0)

    client.unsubscribe(['topic/something/inca/ceva/1234/#'])
    #client.unsubscribe(['topic/#'])
    #client.disconnect()
