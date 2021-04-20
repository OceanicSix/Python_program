#
class MessageBoard:


    def __init__(self,socket):
        self.socket=socket
        self.message=''


    #accessor
    def get_socket(self):
        return self.socket

    def get_message(self):
        return self.message

    #mutator
    def set_message(self,message):
        self.message=message

    def __str__(self):
        pass

    def __contains__(self, item):
        pass

def main():
    pass


if __name__ == '__main__':
    main()

