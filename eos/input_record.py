from AES import AES_encryption
import os
user_name=input("please input user name: ")
first_name=input("please input first name: ")
last_name=input("please input last name: ")
grade=input("please input grade: ")
key=input("please input encryption key: ")



encryption=AES_encryption(key)
ciphertext=encryption.encrypt_string(grade)


command="cleos push action student upsert '["\
        +'"'+user_name+'"'+","+'"'+first_name+'"'+","+'"'+last_name+'"'+","+'"'+ciphertext.decode("utf-8")+'"'+"]' -p "+user_name+"@active"
print(command)
os.system(command)
