# Import statements
import socket
import sys
import time
import random
import datetime

# An array holding 6 lines
lines = ["This is line 0",
        "This is line 1",
        "This is line 2",
        "This is line 3",
        "This is line 4",
        "This is line 5"]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print('['+ str(datetime.datetime.now())+'] Starting streaming server on {}:{}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('['+ str(datetime.datetime.now())+'] Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('['+ str(datetime.datetime.now())+'] Connection from', client_address)
        # Get the random line from lines array
        line = lines[random.randrange(6)]
        connection.sendall(line.encode())
        print ('Data Sent: ' + line)
        time.sleep(5)
    finally:
        # Clean up the connection
        connection.close()