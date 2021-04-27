#!/usr/bin/python3

import fcntl
import struct
import os
import time
from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000
# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack("16sH", b"seana%d", IFF_TUN | IFF_NO_PI)
ifname_bytes = fcntl.ioctl(tun, TUNSETIFF, ifr)
# Get the interface name
ifname = ifname_bytes.decode("UTF-8")[:16].strip("\x00")
print("Interface Name: {}".format(ifname))


os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))
while True:
    packet = os.read(tun,2048)
    ip_pkt = IP(packet)
    print(ip_pkt.summary())


    #------------------------------------------send spoof icmp reply-----------------------------------
    if ip_pkt[IP].proto==1 and ip_pkt[ICMP].type==8:
        print("reach here")
        icmp_reply=IP(dst=ip_pkt.src,src=ip_pkt.dst)/ICMP(type=0,id=ip_pkt[ICMP].id,seq=ip_pkt[ICMP].seq)/ip_pkt[Raw].load
        print(icmp_reply.summary())
        os.write(tun,bytes(icmp_reply))

