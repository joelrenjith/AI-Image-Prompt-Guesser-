from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024

mySocket = socket(AF_INET, SOCK_DGRAM)

mySocket.sendto('Hello!'.encode('utf-8'), (SERVER_IP, PORT_NUMBER))

data = mySocket.recvfrom(SIZE)[0].decode()
print(data)

username = input()
mySocket.sendto(username.encode('utf-8'), (SERVER_IP, PORT_NUMBER))

data = mySocket.recvfrom(SIZE)[0].decode()
print(data)