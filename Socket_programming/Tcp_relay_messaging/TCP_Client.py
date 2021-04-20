import threading
from socket import *
from threading import Timer
from time import sleep




def foo(socket):
    # print("reach here")
        sentence = input()
        if sentence == "q":
            raise KeyboardInterrupt
        else:
            socket.send(sentence.encode())



serverName = "localhost"
serverPort = 12000
## create client socket, first argument indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))



while True:
    try:
        # print("\n new interation")
        t = threading.Thread(target=foo,args=(clientSocket,))
        t.start()
        t.join(3)
        clientSocket.settimeout(1)
        modifiedSentence = clientSocket.recv(2048)
        print("------------------- " + modifiedSentence.decode())
        # print('From Server: ', modifiedSentence.decode())


        #Client receive IpIacIketI fIrIoIm serveIr



    except timeout:
        continue


    except :
        clientSocket.close()
        exit(0)

