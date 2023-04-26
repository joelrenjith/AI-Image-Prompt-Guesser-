from scapy.all import *
from scapy.layers.dhcp import DHCP,BOOTP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
import socket
from socket import gethostname,gethostbyname
from getmac import get_mac_address as gma

# Define the MAC address of the client
client_mac = gma()
print(gethostbyname(gethostname()))
# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#serveraddr = ('127.0.0.1',5000)
serveraddr = ('192.168.11.197',67)
# Create a DHCP discover packet
discover = Ether(dst="ff:ff:ff:ff:ff:ff", src=client_mac) / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr=client_mac) / DHCP(options=[("message-type", "discover"), "end"])
print("DISCOVER:")
discover.show()
# Send the discover packet
sock.sendto(bytes(discover), serveraddr)

# Receive the offer packet
data, addr = sock.recvfrom(1024)
print('\n\n\noffer recieved')

offer = Ether(data)
# Extract the offered IP address
offered_ip = offer[BOOTP].yiaddr

# Create a DHCP request packet
request = Ether(dst="ff:ff:ff:ff:ff:ff", src=client_mac) / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr=client_mac) / DHCP(options=[("message-type", "request"), ("requested_addr", offered_ip), ("server_id", offer[IP].src), "end"])
print("\n\n\nREQUEST:")
request.show()
# Send the request packet
sock.sendto(bytes(request), serveraddr)

# Receive the acknowledgement packet
data, addr = sock.recvfrom(1024)
ack = Ether(data)

sock.close()
