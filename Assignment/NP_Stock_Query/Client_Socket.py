from socket import *

def input_validation(string):
    try:
        if len(string)==0:
            print("please input the valid number"+"\n")
            return False
        if "t=" in string and "d=" not in string:
            print("plIease input the valid number" + "\n")
            return False
        if "d=" in string and "t=" not in string:
            print("please input the valid number" + "\n")
            return False
        argument_list = string.strip().split()
        if "t=" not in argument_list and "d=" in argument_list:
            return False
        if "d=" not in argument_list and "t=" in argument_list:
            return False
        for item in argument_list:
            if "t=" in item or "d=" in item:
                if int(item[2:]) <= 0:
                    print("please input the valid number" + "\n")
                    return False
            elif item not in ["1", "2", "3", "4", "q"]:
                print("please input the valid number" + "\n")
                return False
        return True

    except:
        print("please input the valid number" + "\n")
        return False

chosen_index=""
flag=False
serverName = 'localhost'
serverPort = 12000
## create client socket, first argument indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))

#Client receive packet from server
menu = clientSocket.recv(2048)
print(menu.decode())
while chosen_index!="q":
    try:
        valid = False

        while not valid:
            chosen_index=input("please input the item number here or press 'q' to disconnect: ")
            valid=input_validation(chosen_index)

        if "t=" in chosen_index and "d=" in chosen_index:
            clientSocket.send(chosen_index.encode())
            argument_list = chosen_index.strip().split()
            for item in argument_list:
                if item[:2] == "t=":
                    interval = int(item[2:])
                if item[:2] == "d=":
                    duration = int(item[2:])
            update_times = duration // interval
            for i in range(update_times+1):
                query_result = clientSocket.recv(2048).decode()
                print(query_result)


        elif chosen_index!="q":
            clientSocket.send(chosen_index.encode())
            query_result = clientSocket.recv(2048).decode()
            print(query_result)

        else:
            clientSocket.send(chosen_index.encode())
            clientSocket.close()
    except:
            print("Connection is closed")
            exit(1)