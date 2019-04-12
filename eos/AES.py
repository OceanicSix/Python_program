from Crypto.Cipher import AES
from Crypto.Hash import MD5# MD5 can generate 32byte long key, sha256 will generate 64byte not suit for AES
from Crypto.Hash import SHA256
import base64
import os


class AES_encryption:
    def __init__(self, password, block_size=32, padding="{"):
        # create key and cipher
        key = MD5.new()
        key.update(password.encode("utf-8"))  # convert password from "str" to "byte" type
        self.cipher = AES.new(key.hexdigest())
        self.block_size = block_size
        self.padding = padding

        #for file
        self.iv=os.urandom(16)
        self.cipher_file=AES.new(key.hexdigest(),AES.MODE_CBC,self.iv)

    def encrypt_string(self, message):

        message = message + (self.block_size - len(message) % self.block_size) * self.padding
        encrypted_message = self.cipher.encrypt(message)
        ciphertext = base64.b64encode(encrypted_message)
        return ciphertext

    def decrypt_string(self, ciphertext):
        encrypted_message = base64.b64decode(ciphertext)
        message = self.cipher.decrypt(encrypted_message).decode("utf-8").rstrip(self.padding)  # convert message
        #message = self.cipher.decrypt(encrypted_message)
        # from "byte" to "str"
        return message


    def encrypt_file(self,file_name):
        chunksize=64*1024
        outfile_name=file_name+".enc"
        file_size=str(os.path.getsize(file_name)).zfill(16) #size as byte, zfill to 16
        # so it can be a fixed length ,then read in decryption step
        print(file_size)
        print(self.iv)
        input_file=open(file_name,"rb")
        output_file=open(outfile_name,"wb")
        output_file.write(file_size.encode("utf-8"))
        output_file.write(self.iv)

        while True:
            chunk=input_file.read(chunksize)
            if len(chunk)==0:
                break
            elif len(chunk)%self.block_size !=0:
                chunk+=b" "*(self.block_size-len(chunk)%self.block_size)
            output_file.write(self.cipher_file.encrypt(chunk))

    def decrypt_file(self,file_name):
        chunksize=64*1024
        outfile_name=file_name+".dec"
        input_file=open(file_name,"rb")
        file_size=int(input_file.read(16))
        iv=input_file.read(16)
        print(file_size,iv==self.iv)
        output_file=open(outfile_name,"wb")
        while True:
            chunk=input_file.read(chunksize)
            if len(chunk)==0:
                break
            output_file.write(self.cipher_file.decrypt(chunk))
        output_file.truncate(file_size)




if __name__ == '__main__':
    a_encryption = AES_encryption("89757")
    ciphertext = a_encryption.encrypt_string("abc")
    print(ciphertext)
    print(a_encryption.decrypt_string(ciphertext))
    # a_encryption.encrypt_file("file")
    # a_encryption.decrypt_file("file.enc")


