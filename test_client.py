import sys
from socket import socket, AF_INET, SOCK_DGRAM
SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
try:
    mySocket = socket( AF_INET, SOCK_DGRAM )
    username = input('enter username')
    # myMessage = "Hello!"
    myMessage1 = ""
    i = 0
    while i < 10:
        mySocket.sendto(username.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        i = i + 1

    mySocket.sendto(username.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    ans  = mySocket.recv(1024)
    print(ans.decode())
except Exception as e:
    print(e)
