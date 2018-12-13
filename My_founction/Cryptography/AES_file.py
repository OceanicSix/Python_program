from AES import AES_encryption

a_encryption=AES_encryption("89757")

input_file=open("123","rb")
output_file=open("output","wb+")

while True:
    buffer=input_file.read(64*1024)

    if len(buffer)==0:
        break
    # elif len(buffer) % 16 != 0:
    #     buffer = buffer.decode("utf-8")+' ' * (16 - len(buffer) % 16)
    output_file.write(a_encryption.encrypt(buffer))



decrypte_file=open("decrypte","wb")
while True:
    buffer = output_file.read(64 * 1024)
    if len(buffer) == 0:
        break
    decrypte_file.write(a_encryption.decrypt(buffer))