import time

from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('broker.mqttdashboard.com', 1883, 5, 1, "Last Will", "E DE JALE!", 1, 1)

    client.publish('testtopic/foarte/interesant/poate/merge/testQOS0', 'message', 0, 0, 0)
    client.publish('calin', 'message', 2, 0, 1)
    client.subscribe(['calin'], [2])
    #client.publish('testtopic/foarte/interesant/poate/merge/testQOS0', "mesajJMECKER", 0, 0, 0)
    #time.sleep(1)
    #client.publish('testtopic/foarte/interesant/poate/merge/testQOS1', "mesajSiMaiJmeckerQOs1", 1, 0, 0)
    #time.sleep(1)

    #client.unsubscribe(['topic/something/inca/ceva/1234/#'])
    #client.unsubscribe(['topic/#'])
    #client.disconnect()