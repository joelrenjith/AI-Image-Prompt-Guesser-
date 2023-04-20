from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import os
import pandas as pd
from test_selenium_thread import sel_thread
from threading import Thread
from server import convert
import re
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '0.0.0.0' )
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
players = {}
bit  = 0
c = 0
ready_list = []
def listen():
    global bit
    while(1):
        if bit ==1:
            sendeveryone('__')
            return
        msg,id = mySocket.recvfrom(SIZE)
        msg = msg.decode()
        if bit ==0:
            if msg!='1':
                lobby(id,msg)
            else:
                ready(id)
    
        

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
        mySocket.sendto(str(ready_list).encode(),id)

        players[id] = username
        # os.system('cls')

        
        print(id,':',username)
        sendeveryone(username)
        print('sent lobby')
        
       
        

def ready(id):
    global players,c,bit,ready_list
    print('recived a ready from',players[id])

    if id in players:
        c+=1
        sendeveryone('ready')
        sendeveryone(str(list(players).index(id)))
        ready_list.append(str(list(players).index(id)))
        if c == len(players):
            bit = 1

def start_game():
    global players
    
    leaderboard = {}
    for i in players:
        leaderboard[players[i]] = 0
    Thread(target=sel_thread).start()
    df = pd.read_csv('words&imgs.csv')
    for x in range(0,3):
        point = len(players)
        s = df['string'][0]
        print(s)
        img_link = df['link'][0]
        print(img_link)
        copy = ''
        vowel = ['a','e','i','o','u']
        for i in s:
            if i != ' ':
                if i not in vowel:
                    copy+='_'
                else:
                    copy+=i
            else:
                copy+=i
        
        sendeveryone(convert(copy))
        sendeveryone(img_link)
        while(1):
            check,addr = mySocket.recvfrom(SIZE)
            check = check.decode().lower()
            if check == '__':
                sendeveryone(s)
                sendeveryone(str(leaderboard))
                break
            if check ==s:
                leaderboard[players[addr]] += point
                point = point - 1
                msg = players[addr]+' goddit!!'
                sendeveryone(msg)
                # mySocket.sendto(s.encode('utf-8'),(addr))
                if point ==0:
                    sendeveryone(s)
                    sendeveryone(str(leaderboard))
                    break
            else:
                if check in s and len(check)>0:
                    print(copy)
                    for m in re.finditer(check, s):
                        print(check, 'matched from position', m.start(), 'to', m.end())
                    copy  = copy.replace(copy[m.start():m.end()],check)
                    print(copy)
                if copy == s:
                    # mySocket.sendto(s.encode('utf-8'),(addr))
                    leaderboard[players[addr]] += point
                    point = point - 1
                    msg = players[addr]+' goddit!!'
                    sendeveryone(msg)
                    # mySocket.sendto(s.encode('utf-8'),(addr))
                    if point ==0:
                        sendeveryone(s)
                        sendeveryone(str(leaderboard))
                        break
                else:    
                    sendeveryone(players[addr]+' : '+check)
                mySocket.sendto(convert(copy).encode('utf-8'),(addr))
    sendeveryone('!!')    
    
listen()
start_game()
    



