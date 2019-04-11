from aes import AES_encryption

# user_name=input("user name: ")
# seach_attr=input("seach attribute is: ")
decryption_key=input("please input decryption key: ")

decryption=AES_encryption(decryption_key)

encrypted_record=['bo', 'yang', b'egwCUZ7cST1JhDNqDZq6xbWSTLVg5yP5R0tL1rIKOpA=']
output=""
output+="first name: "+encrypted_record[0]+"\n"\
        "last name: "+encrypted_record[1]+"\n"\
        "grade: "+decryption.decrypt_string(encrypted_record[2])
print(output)
