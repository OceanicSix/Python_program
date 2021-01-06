from scapy.all import *
a=IP()
a.dst="8.8.8.8"
for ttl in range(1,20):
    a.ttl=ttl
    b = ICMP()
    p = a / b
    send(p)


