from socket import *
serverName = '45.76.123.227'
serverPort = 9000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message =input("Input lowercase sentence:" )
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()