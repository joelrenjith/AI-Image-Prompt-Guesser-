from socket import socket, AF_INET, SOCK_DGRAM
import threading

PORT_NUMBER = 5000
SIZE = 1024

def multi_threaded_client(connection):
    mySocket.sendto(('Enter username: ').encode(), connection)
    username = mySocket.recvfrom(SIZE)[0].decode()
    usernames.append(username)
    mySocket.sendto(('Your username is: ' + username).encode(), connection)

hostName = '0.0.0.0'
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

usernames = []

print("Server listening on port {0}\n".format(PORT_NUMBER))

while True:
    data, address = mySocket.recvfrom(SIZE)
    threading.Thread(target=multi_threaded_client, args=(address,)).start()