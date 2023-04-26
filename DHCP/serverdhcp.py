from scapy.all import *
from scapy.layers.dhcp import DHCP, BOOTP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
import socket
from socket import gethostname, gethostbyname
from getmac import get_mac_address as gma

# Define the MAC address of the server and the IP address to offer
server_mac = gma()
offered_ip = "192.168.1.100"
ip = gethostbyname(gethostname())
# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
sock.bind(('', 67))
print('listenig')
# Create an empty list to store the client pool
client_pool = []

while True:
    # Receive a packet
    data, addr = sock.recvfrom(1024)
    
    pkt = Ether(data)

    # Check if it is a DHCP discover packet
    if DHCP in pkt and pkt[DHCP].options[0][1] == 1:
        # Create a DHCP offer packet
        offer = Ether(dst=pkt[Ether].src, src=server_mac) / IP(src=ip, dst='255.255.255.255') / UDP(sport=67, dport=68) / BOOTP(op=2, yiaddr=offered_ip, siaddr=ip, chaddr=pkt[Ether].src) / DHCP(options=[("message-type", "offer"), ("server_id", ip), ("lease_time", 43200), "end"])
        print("OFFER:")
        offer.show()
        # Send the offer packet
        print(addr[0])
        sock.sendto(bytes(offer), (addr))
        print('sent offer')

    # Check if it is a DHCP request packet
    elif DHCP in pkt and pkt[DHCP].options[0][1] == 3:
        # Create a DHCP acknowledgement packet
        ack = Ether(dst=pkt[Ether].src, src=server_mac) / IP(src=ip, dst='255.255.255.255') / UDP(sport=67, dport=68) / BOOTP(op=2, yiaddr=offered_ip, siaddr=ip, chaddr=pkt[Ether].src) / DHCP(options=[("message-type", "ack"), ("server_id", ip), ("lease_time", 43200), "end"])
        print("\n\n\nACK:")

        ack.show()
        # Send the acknowledgement packet
        sock.sendto(bytes(ack), (addr))

        # Add the client's address and port number to the client pool
        client_pool.append(addr)
    # else:
    #     print("couldnt find")

sock.close()