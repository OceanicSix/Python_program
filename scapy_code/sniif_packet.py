from scapy.all import *

def print_pkt(pkt):

    print("---------------this is a new packet----------------------")
    pkt.show()

pkt=sniff(filter= "icmp and host 192.168.0.6 " , prn=print_pkt)
