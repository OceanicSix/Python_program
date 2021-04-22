import threading
from socket import *

serverName = "localhost"
serverPort = 12000
## create client socket, first argument indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))
message = input("type message here...")
clientSocket.send(message.encode())
clientSocket.close()
