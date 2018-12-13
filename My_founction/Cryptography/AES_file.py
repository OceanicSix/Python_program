from AES import AES_encryption

a_encryption=AES_encryption("89757")

input_file=open("123","rb")
output_file=open("output","wb")

while True:
    buffer=input_file.read(64*1024)
    print(type(buffer))
    if len(buffer)==0:
        break
    #output_file.write(a_encryption.encrypt(buffer))