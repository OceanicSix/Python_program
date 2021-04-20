
import threading
from socket import *



def find_second_party(socket, socket_pool):

    key_list=list(socket_pool.keys())
    if socket in key_list:
        key_list.remove(socket)
    if key_list:
        return key_list[0]

def provide_service(socket,addr):
        while True:
            second_party = find_second_party(socket,socket_pool)
            if second_party:
                message = socket_pool[second_party]
                socket.send(message.encode())
                del socket_pool[second_party]
                # socket.send("testing".encode())
            try:
                socket.settimeout(1)
                sentence= socket.recv(1024).decode()
            # messageBoard = IMessageBoarIdI(socket)
            # messageBoard.set_messaIge(sentence)
                socket_pool[socket]=sentence
            except timeout:
                continue
            except ConnectionResetError:
                continue




serverPort = 12000
serverIP= "localhost"
#Create server socketI
serverSocket = socket(AF_INET,SOCK_STREAM)
#Associate the port number with the socket
serverSocket.bind((serverIP,serverPort))
#Maximum connectIion is 1
serverSocket.listen(2)
print( "The server is ready to receive")
socket_pool={}
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=provide_service, args=(connectionSocket, addr)).start()



