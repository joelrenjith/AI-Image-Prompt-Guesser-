from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys, threading
PORT_NUMBER = 5656
SIZE = 1024
connected = []
try:
    def multi_threaded_client(connection,username):
        print(connection)
        mySocket.sendto(('okay your user name is ='+username).encode(),(connection))
        

        print('recieved username',username)
        
    ThreadCount = 0
    hostName = gethostbyname( '0.0.0.0' )
    mySocket = socket( AF_INET, SOCK_DGRAM )
    mySocket.bind( (hostName, PORT_NUMBER) )



       
    print ("Test server listening on port {0}\n".format(PORT_NUMBER))
    s = "bye"
    while True:
        Client, address = mySocket.recvfrom(1024)
        if address not in connected:
            connected.append(address)
            print(Client.decode())
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            
            threading.Thread(target = multi_threaded_client,args= (address,Client.decode(),)).start()
            
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))

except Exception as e:
    print(e)