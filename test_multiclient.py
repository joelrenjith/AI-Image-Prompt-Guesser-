from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname( '0.0.0.0' )
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
players = {}
bit  = 0
def lobby():
    global players
    while(1):
        global bit
        if bit ==1:
            return
        username,id = mySocket.recvfrom(SIZE)
        if id not in players:
            players[id] = username

def ready():
    c = 0
    global players
    while(c!=len(players)):
        msg,id = mySocket.recvfrom(SIZE)
        if id in players:
            c = c+1
    bit = 1



    



