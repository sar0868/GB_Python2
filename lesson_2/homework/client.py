
# Клиент игры "Запоминалка"

import socket
import string
import random
import datetime

class Transaction():

    def __init__(self):
        pass

    def pack(self):
        # title = '{}'.format(bin('zz'))
        data = datetime.datetime.today()
        yearT = '{:07b}'.format(data.year - 2000)
        dayT = '{:05b}'.format(data.day)
        monthT = '{:04b}'.format(data.month)
        data_trans = ''.join(yearT,monthT,dayT)
        return data_trans



def randstring(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])


def packet_transaction():
    data = randstring(100)
    title = '0x7A7A'
    data_trans = datetime.datetime.today()
    res = bytes('{}{}{}'.format(title, data_trans, data),'utf-8')
    return res


HOST, PORT = 'localhost', 9999

print('Клиент запущен')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(packet_transaction())

recvd = str(sock.recv(1024), 'utf-8')

print(recvd)

sock.close()

# __add__  ->  +