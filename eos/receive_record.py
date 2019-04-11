from AES import AES_encryption
import json
import os

user_name=input("user name: ")
command="cleos get table student student table --"+user_name+" --limit 1 > output.json"
os.system(command)



file=open("output.json","r")
data=json.load(file)
for record in data["rows"]:
    print("first name: "+record["first_name"])
    print("last name: "+record["last_name"])
    print("grade:"+record["grade"])


decryption_key=input("please input decryption key: ")
decryption=AES_encryption(decryption_key)

for record in data["rows"]:
    print("first name: "+record["first_name"])
    print("last name: "+record["last_name"])
    print("grade:"+decrypt_string(bytes(record["grade"],encoding="utf-8")))