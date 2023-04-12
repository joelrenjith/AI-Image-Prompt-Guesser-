from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys, threading
PORT_NUMBER = 5000
SIZE = 1024
try:
    ThreadCount = 0
    hostName = gethostbyname( '0.0.0.0' )
    mySocket = socket( AF_INET, SOCK_DGRAM )
    mySocket.bind( (hostName, PORT_NUMBER) )

    def multi_threaded_client(connection):
        mySocket.sendto(str.encode('enter username:'),(connection))
        username  = mySocket.recv(1024)
        mySocket.sendto(str.encode('ok,your username is '+username),(connection))

       
    print ("Test server listening on port {0}\n".format(PORT_NUMBER))
    s = "bye"
    while True:
        Client, address = mySocket.recvfrom(1024)
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        threading.start_new_thread(multi_threaded_client, (Client,address ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

except Exception as e:
    print(e)