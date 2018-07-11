from socket import *
from Server_function import Stock_Server
import threading
import time



#
class Connection:
    def __init__(self):

        self.server = Stock_Server()

        self.serverPort = 12000
        # Create server socket

        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # Associate the port number with the socket, and enable the socket can be reused
        self.serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.serverSocket.bind(('localhost', self.serverPort))
        # Maximum connection is 2

    def listen(self):
        self.serverSocket.listen(2)
        print("The server is ready to receive")
        while True:
            connectionSocket, addr = self.serverSocket.accept()
            connectionSocket.settimeout(30)
            threading.Thread(target=self.provide_service, args=(connectionSocket, addr)).start()


    def show_menu(self):
        menu_message = "Below is the stock menu, please choose the item number you would like to query" + "\n"
        menu_message += str(self.server)
        return menu_message

    # Send both the result and newest menu info
    def show_query(self, index):
        red = "\033[31m"
        white = "\033[0m"
        query_result="\n" + red + "Here is the result:"+"\n"+"item name"+"\t"+"item color"+"\t"\
                    + "price"+"\t"+"highest buy"+"\n"
        index_list=index.strip().split()
        for item in index_list:
            if "t=" not in item and "d=" not in item:
                query_result += red+self.server.stock_query(int(item)) \
                                + "\n" + "\n" + white
        query_result+=self.show_menu()
        return query_result

    def show_update(self,index,times):
        red = "\033[31m"
        white = "\033[0m"
        query_result = ''
        index_list = index.strip().split()
        for item in index_list:
            if "t=" not in item and "d=" not in item:
                query_result += "\n" + red + "Here is the update"+str(times)+"\t" + self.server.stock_query(int(item)) \
                                + "\n" + "\n" + white+"\n"+"-------------------------"
        return query_result


    def provide_service(self, connectionSocket, addr):
        while True:
            try:
                chosen_index = ""

                print("establish connection with " + str(addr))
                connectionSocket.send(self.show_menu().encode())
                while chosen_index != "q":
                    chosen_index = connectionSocket.recv(1024).decode()

                    #Achieve the update function
                    if "t=" in chosen_index and "d=" in chosen_index:
                        argument_list=chosen_index.strip().split()
                        for item in argument_list:
                            if item[:2]=="t=":
                                interval=int(item[2:])
                            if item[:2]=="d=":
                                duration=int(item[2:])
                        update_times= duration//interval
                        #time.sleep(interval)
                        for i in range(update_times):
                            connectionSocket.send(self.show_update(chosen_index,i+1).encode())
                            #the last time won't wait
                            if i!=update_times-1:
                                time.sleep(interval)
                        connectionSocket.send(self.show_menu().encode())

                    elif chosen_index != "q":
                        connectionSocket.send(self.show_query(chosen_index).encode())


                    else:
                        connectionSocket.close()
                        print("connection with " + str(addr) + " closed")
                        return None
            except:
                connectionSocket.close()
                print("connection with " + str(addr) + " closed")
                return None







def main():
    a = Connection()
    a.listen()



if __name__ == '__main__':
    main()
