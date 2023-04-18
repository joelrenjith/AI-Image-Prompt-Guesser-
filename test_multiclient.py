import os
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
PORT_NUMBER = 5000
SIZE = 1024
hostName = '127.0.0.1'
# mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket = socket( AF_INET, SOCK_DGRAM )
adr = (hostName,PORT_NUMBER)
user = input('enter username')
mySocket.sendto(user.encode(),adr)
print('list of players:\n__________________________________')
while(1):
    print(mySocket.recv(SIZE).decode())
print('______________________________')
