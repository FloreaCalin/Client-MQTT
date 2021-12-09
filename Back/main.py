import time

from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('broker.mqttdashboard.com', 1883, 255, 1, 1, None, None, None)
    #client.pingreq()

    client.publish('topic', "akhf", 1, 0, 0)
    client.subscribe(['testtopic/#', 'testtopic/DaHaKa_home/#', 'topic/#'], [1, 2, 1])

    time.sleep(3)
    client.unsubscribe(['testtopic/#'])
