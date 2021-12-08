from Back.client import Client

if __name__ == '__main__':
    client = Client (20, 'calin', 'parola')
    client.connect('localhost', 1883, 65535, None, None, None, 1, 0)