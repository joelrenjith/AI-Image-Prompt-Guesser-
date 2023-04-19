import os
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import threading
PORT_NUMBER = 5000
SIZE = 1024
hostName = '192.168.11.197'
# hostName = '127.0.0.1'
# mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket = socket( AF_INET, SOCK_DGRAM )
adr = (hostName,PORT_NUMBER)
user = input('enter username')
mySocket.sendto(user.encode(),adr)

def ready():
    # one  = input('enter 1 to get ready')
    mySocket.sendto('1'.encode(),adr)
    # return

# t1 = threading.Thread(target=ready())
# t1.start()

print('list of players:\n__________________________________')
while(1):
    msg  = mySocket.recv(SIZE).decode()
    if msg=='__':
        break
    print(msg)
print('______________________________')
