import threading
from socket import *





serverName = "45.76.123.227"
serverPort = 12000
## create client socket, first argument indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))
sentence=''
while True:
    try:
        sentence += input("")+"\n"
    except EOFError:
        clientSocket.send(sentence.encode())
        break
print("sending complete")
clientSocket.close()
