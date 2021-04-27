from scapy.all import *

def print_pkt(pkt):

    print("---------------this is a new packet----------------------")

    new_pkt = pkt[IP]
    if new_pkt[ICMP]:
        new_pkt.show()

sniff(filter= "icmp" , prn=print_pkt)
