from scapy.all import *
from scapy.layers.inet import IP, ICMP, UDP

# spoof IP

# a=IP()
# a.dst="10.0.2.3"
# b=ICMP()
# p=a/b
# send(p)


# Spoof UDP

ip=IP(src="8.8.8.8",dst="seanyiyi.com")

udp= UDP(sport = 8888, dport = 9000)

data="hello/n"
pkt = ip/udp/data
send(pkt,verbose=0)

