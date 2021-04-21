import threading
from socket import *

def provide_service(socket, addr):
    while True:
        message= socket.recv(1024)
        if message:
            print(message.decode())
serverPort = 12000
#Create server socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#Associate the port number with the socket
serverSocket.bind(('localhost',serverPort))
#Maximum connection is 1
serverSocket.listen(2)
print( "The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=provide_service, args=(connectionSocket, addr)).start()

