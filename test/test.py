from scapy.all import *
a=IP()

a.src=RandIP()
a.dst="10.0.2.3"
b=ICMP()


p=a/b
send(p)