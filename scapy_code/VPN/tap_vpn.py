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
ifr = struct.pack("16sH", b"tap%d", IFF_TAP | IFF_NO_PI)
ifname_bytes = fcntl.ioctl(tun, TUNSETIFF, ifr)
# Get the interface name
ifname = ifname_bytes.decode("UTF-8")[:16].strip("\x00")
print("Interface Name: {}".format(ifname))


os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))
while True:
    packet = os.read(tun,2048)
    ether = Ether(packet)
    print(ether.summary())

    # Send a spoofed ARP response
    if ARP in ether and ether[ARP].op == 1:
        arp = ether[ARP]
        newether = Ether(src="aa:bb:cc:dd:ee:ff",dst=arp.hwsrc)
        newarp = ARP(op=2,psrc=arp.pdst,hwsrc="aa:bb:cc:dd:ee:ff",pdst=arp.psrc,hwdst=arp.hwsrc )
        newpkt = newether / newarp
        print("***** Fake response: {}".format(newpkt.summary()))
        os.write(tun, bytes(newpkt))


