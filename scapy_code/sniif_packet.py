from scapy.all import *

def print_pkt(pkt):

    print("---------------this is a new packet----------------------")

    new_pkt = pkt[IP]
    new_pkt.show()

sniff(filter= "host seanyiyi.com" , prn=print_pkt)
