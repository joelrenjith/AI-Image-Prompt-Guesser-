from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname( '0.0.0.0' )
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
players = {}
bit  = 0
c = 0

def listen():
    while(1):
        msg,id = mySocket.recvfrom(SIZE)
        if bit ==0:
            if msg!=1:
                lobby(id,msg)
            else:
                ready(id)
        




def lobby(id,username):
    global players
    if id not in players:
        players[id] = username

def ready(id):
    global players,c
    if id in players:
        c+=1
        if c == len(players):
            bit = 1



    



