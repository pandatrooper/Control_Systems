from scapy.all import *
from pymodbus.client.sync import ModbusTcpClient

from scapy.all import *
import time

class Modbus(Packet):
    name = "Modbus"
    fields_desc = [ XByteField("Function Code", int('05', 16)),
                    ShortField("Reference Number", int('0001', 16)),
                    ShortField("Data", int('ff00', 16))                  
                    ]
                    
class Modbus0(Packet):
    name = "Modbus"
    fields_desc = [ XByteField("Function Code", int('05', 16)),
                    ShortField("Reference Number", int('0001', 16)),
                    ShortField("Data", int('0000', 16))                  
                    ]


class ModbusTCP(Packet):
    name = "Modbus/TCP"
    fields_desc = [ ShortField("Transaction Identifier", 66),
                    ShortField("Protocol Identifier", 0),
                    ShortField("Length", 6),
                    XByteField("Unit Identifier",0)
                    ]       

srcIP = "192.168.1.2"
destIP = "192.168.1.250"
srcmac = "90:2e:16:d4:21:7a"
destmac = "00:80:f4:52:26:8c"
leng = 111
i_d = int('7b40', 16)
ip_flags = 40
ttl = 128
ip_chksum = int('0000', 16)
seq = int('51ae9538', 16)            
ack = int('10626181', 16)
tcp_flags = 'AP'
window = 1055
tcp_chksum = int('8511', 16)
urgptr = 0 
srcPort = 53268
destPort= 502

# Create a socket and connect
s = socket.socket()
s.connect(("192.168.1.251", 502))   # IP and port
ss = StreamSocket(s, Raw)

while True:
    try:
        # Encapsulate modbus inside the raw data, then send and receive
        # Anything can be done with response
       ss.sr1(Raw(ModbusTCP()/Modbus()), timeout=1)
       time.sleep(0.15)
       ss.sr1(Raw(ModbusTCP()/Modbus0()), timeout=1)
       time.sleep(0.15)
    except KeyboardInterrupt:
       break

#pkt = Ether(src=srcmac, dst=destmac) / IP(src=srcIP, dst=destIP, len=leng, id=i_d, flags=ip_flags, ttl=ttl, chksum=ip_chksum) / TCP(sport=srcPort, dport=destPort, seq=seq, ack=ack, flags=tcp_flags, window=window, chksum=tcp_chksum, urgptr=urgptr) / ModbusTCP() / Modbus()

#sendp(pkt)
