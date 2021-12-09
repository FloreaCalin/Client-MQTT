import time

from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('localhost', 1883, 255, 1, None, None, None, None)
    client.pingreq()
    #time.sleep(5)
    client.publish('topic', "akhf", 1, 20)
