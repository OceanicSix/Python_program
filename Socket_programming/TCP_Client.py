import threading
from socket import *

serverName = "seanyiyi.com"
serverPort = 9090
## create client socket, firIst argumIent indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))
message = input("type message here...")
clientSocket.send(message.encode())

textFromServer = clientSocket.recv(1024).decode()
print("Text from server is: "+textFromServer)
clientSocket.close()
