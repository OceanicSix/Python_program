from scapy.all import *
from scapy.layers.inet import IP, ICMP, UDP

# spoof IP

# a=IP()
# a.dst="10.0.2.3"
# b=ICMP()
# p=a/b
# send(p)


# Spoof UDP

ip=IP(src = "210.49.192.134", dst="45.76.123.227")

udp= UDP(sport = 8888, dport = 9000)

data="hello/n"
pkt = ip/udp/data
send(pkt,verbose=0)