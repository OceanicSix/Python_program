#!/usr/bin/python3
import select
import fcntl
import struct
import os
import time
from scapy.all import *
from socket import *

TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000
# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack("16sH", b"tun%d", IFF_TUN | IFF_NO_PI)
ifname_bytes = fcntl.ioctl(tun, TUNSETIFF, ifr)
# Get the interface name
ifname = ifname_bytes.decode("UTF-8")[:16].strip("\x00")
print("Interface Name: {}".format(ifname))


os.system("ip addr add 192.168.53.100/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))
os.system("ip route add 192.168.53.0/24 dev {}".format(ifname))

#------------------------------------receive packet from socket or tun----------
IP_A = "0.0.0.0"
PORT = 9090
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((IP_A, PORT))



ip=""
port=""
while True:
# this will block until at least one interface is ready
    ready, _, _ = select.select([sock, tun], [], [])

    for fd in ready:
        if fd is sock:
            data, (ip, port) = sock.recvfrom(2048)
            pkt = IP(data)
            print("From socket ----: {} --> {}".format(pkt.src, pkt.dst))
            os.write(tun,data)


        if fd is tun and port:
            packet = os.read(tun, 2048)
            pkt = IP(packet)
            print("From tun ----: {} --> {}".format(pkt.src, pkt.dst))
            sock.sendto(packet,(ip,port))

