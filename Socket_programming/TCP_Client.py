from socket import *
serverName = '118.138.218.141'
serverPort = 12000
## create client socket, first argument indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
#Client receive packet from server
modifiedSentence = clientSocket.recv(2048)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()