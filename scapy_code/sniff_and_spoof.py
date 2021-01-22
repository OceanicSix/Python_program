from scapy.all import *

def spoof_pkt(pkt):
    print("-----------------sniffed packet-----------")
    pkt.show()

    targetIP=pkt[IP].src
    spoofPkt=IP()
    spoofPkt.src=pkt[IP].dst
    spoofPkt.dst=targetIP
    icmpPayload=ICMP(type=0,id=pkt[ICMP].id,seq=pkt[ICMP].seq)
    p=spoofPkt/icmpPayload/pkt[Raw].load

    print("-----------------spoofed packet-----------")
    p.show()
    send(p)

ifacevalue="Qualcomm Atheros AR956x Wireless Network Adapter"
sniff(iface=ifacevalue, filter= "icmp[icmptype]=icmp-echo" , prn=spoof_pkt)
