from scapy.all import *

def print_pkt(pkt):

    print("---------------this is a new packet----------------------")
    pkt.show()

pkt=sniff(filter= "icmp and src host 49.127.19.58 " , prn=print_pkt)
