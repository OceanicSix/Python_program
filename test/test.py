from scapy.all import *

def print_pkt(pkt):

    print("---------------this is a new packet----------------------")
    pkt.show()

pkt=sniff( prn=print_pkt)
