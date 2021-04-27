from socket import *
serverPort = 12000
clientAddress="localhost"
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("localhost", serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(clientAddress)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)