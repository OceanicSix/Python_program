#!/usr/bin/python3

import socket, ssl, sys, pprint

hostname = sys.argv[1]
port = 443
cadir = 'D:\Google Drive\Study\S1\Python\PY program\Socket_programming\certs'
#cafile="D:\Google Drive\Study\S1\Python\PY program\Socket_programming\certs\DigiCert_Global_Root_CA.pem"

# Set up the TLS context
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) # For Ubuntu 20.04 VM
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)      # For Ubuntu 16.04 VM


context.load_verify_locations(cafile=None, capath=cadir, cadata=None)   #CA certificate
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True                 #check whether hostname in argument match common name in cert

# Create TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))
input("After making TCP connection. Press any key to continue ...")

# Add the TLS
ssock = context.wrap_socket(sock, server_hostname=hostname,
                            do_handshake_on_connect=False)
ssock.do_handshake()   # Start the handshake
print("=== Cipher used: {}".format(ssock.cipher()))
print("=== Server hostname: {}".format(ssock.server_hostname))
print("=== Server certificate:")
pprint.pprint(ssock.getpeercert())
pprint.pprint(context.get_ca_certs())
input("After TLS handshake. Press any key to continue ...")


request = b"GET / HTTP/1.0\r\nHost: " + \
            hostname.encode('utf-8') + b"\r\n\r\n"
ssock.sendall(request)
# Read HTTP Response from Server
response = ssock.recv(2048)
while response:
    pprint.pprint(response)
    response = ssock.recv(2048)

# Close the TLS Connection
ssock.shutdown(socket.SHUT_RDWR)
ssock.close()

