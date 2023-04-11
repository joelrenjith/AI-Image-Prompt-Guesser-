from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024
try:
    hostName = gethostbyname( '0.0.0.0' )
    mySocket = socket( AF_INET, SOCK_DGRAM )
    mySocket.bind( (hostName, PORT_NUMBER) )


    print ("Test server listening on port {0}\n".format(PORT_NUMBER))
    s = "bye"

    (data,addr) = mySocket.recvfrom(SIZE)
    print(addr)
    s = 'bread fire alarm'
    vowel = ['a','e','i','o','u']
    copy  =''
    for i in s:
        if i != ' ':
            if i not in vowel:
                copy+='_'
            else:
                copy+=i
        else:
            copy+=i+' '
        copy+=' '

    mySocket.sendto(copy.encode('utf-8'),(addr))
    print('sent strig')
    while(1):
            check,addr = mySocket.recvfrom(SIZE)
            if check.decode()==s:
                msg = 'you goddit!!'
                mySocket.sendto(msg.encode('utf-8'),(addr))
                break
            else:
                mySocket.sendto(check,(addr))
    mySocket.sendto(s.encode('utf-8'),(addr))
except Exception as e:
    print(e)