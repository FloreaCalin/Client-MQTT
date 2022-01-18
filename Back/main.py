import time

from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('broker.mqttdashboard.com', 1883, 100, 1, "Last Will", "E DE JALE!", 1, 1)

    client.publish('testtopic/foarte/interesant/poate/merge/testQOS0', 'message', 0, 0, 0)
    client.subscribe(['testtopic/foarte/interesant/poate/merge/#'], [2])
    #time.sleep(3)
    #client.publish('testtopic/foarte/interesant/poate/merge/testQOS0', "mesajJMECKER", 0, 0, 0)
    #time.sleep(1)
    #client.publish('testtopic/foarte/interesant/poate/merge/testQOS1', "mesajSiMaiJmeckerQOs1", 1, 0, 0)
    #time.sleep(1)
    #client.publish('testtopic/foarte/interesant/poate/merge/testQOS2', "mesajSiMaiJmecker", 2, 0, 0)

    #client.unsubscribe(['topic/something/inca/ceva/1234/#'])
    #client.unsubscribe(['topic/#'])
    #client.disconnect()