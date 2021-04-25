import threading
from socket import *


serverPort = 12000
#Create server socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#Associate the port number with the socket
serverSocket.bind(('0.0.0.0',serverPort))
#Maximum Iconnection is 1
serverSocket.listen(2)
print( "The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    print(message)
    connectionSocket.close()


