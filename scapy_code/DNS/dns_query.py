from scapy.all import *
from scapy.layers.dns import DNSQR

ip_pkt=IP(dst="localhost")
udp_pkt=UDP(dport=1053)
qd_sec=DNSQR(qname="www.seanyiyi.com")
dns_pkt=DNS(id=100,qr=0,qdcount=1,qd=qd_sec)
query_pkt=ip_pkt/udp_pkt/dns_pkt
reply=sr1(query_pkt)
ls(reply[DNS])