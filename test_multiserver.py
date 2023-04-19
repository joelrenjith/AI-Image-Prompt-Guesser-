from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import os
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '0.0.0.0' )
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
players = {('127.0.0.1',5490):'joel'}
bit  = 0
c = 0

def listen():
    global bit
    while(1):
        msg,id = mySocket.recvfrom(SIZE)
        msg = msg.decode()
        if bit ==0:
            if msg!=1:
                lobby(id,msg)
            else:
                ready(id)
        else: 
            sendeveryone('__')

def sendeveryone(msg):
    global players
    for id in players:
        mySocket.sendto(msg.encode(),id)       
        




def lobby(id,username):
    global players
    if id not in players:
        mySocket.sendto(str(len(players)).encode(),id)
        for i in players:
            mySocket.sendto(players[i].encode(),id)


        players[id] = username
        # os.system('cls')

        
        print(id,':',username)
        sendeveryone(username)
        print('sent lobby')
        
       
        

def ready(id):
    global players,c,bit
    if id in players:
        c+=1
        sendeveryone('ready')
        sendeveryone(str(list(players).index(id)))
        if c == len(players):
            bit = 1

listen()

    



