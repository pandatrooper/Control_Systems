#!/usr/bin/sudo python
import binascii
from scapy.all import *
from scapy import route
from scapy.layers.inet import Ether,IP,UDP

# Connection routes
from scapy.layers.inet import TCP


conf.L3socket = L3RawSocket

srcIP = "127.0.0.1"
destIP = "127.0.0.1"
srcPort = random.randint(1024,65535)
destPort= 502

# TCP SYN
ip=IP(src=srcIP, dst=destIP)
SYN=TCP(sport=srcPort, dport=destPort, flags="S", seq=100)
SYNACK=sr1(ip/SYN, timeout = 10)

# TCP ACK
my_ack = SYNACK.seq + 1
ACK=TCP(sport=srcPort, dport=destPort, flags="A", seq=101, ack=my_ack)

# Custom modbus packet
raw_payload = '00010000000601020001000F' # This is the 12 bytes modbus packet!
payload = binascii.unhexlify(raw_payload)
PUSH=TCP(sport=srcPort, dport=destPort, flags="", seq=101, ack=my_ack)
send(ip/PUSH/payload)


FIN=TCP(sport=srcPort, dport=destPort, flags="FA", seq=101, ack=my_ack)
FINACK=sr1(ip/FIN, timeout = 10)
LASTACK=TCP(sport=srcPort, dport=destPort, flags="A", seq=101, ack=FINACK.seq + 1)
send(ip/LASTACK)