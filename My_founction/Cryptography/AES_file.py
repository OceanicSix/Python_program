import os, sys
from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Hash import MD5

input_file = open("123", "rb")
output_file = open("output", "wb")

decrypted_file = open("decrypted", "wb")

password = "89757"
key = MD5.new()
key.update(password.encode("utf-8"))  # convert password from "str" to "byte" type
iv = os.urandom(16)
cipher = AES.new(key.hexdigest(), AES.MODE_CFB, iv)
encrypted = cipher.encrypt(input_file.read())
output_file.write(encrypted)
output_file.close()

encrypted_file = open("output", "rb")
data = encrypted_file.read()
print(data)
decrypted = cipher.decrypt(data)
print(decrypted)
decrypted_file.write(decrypted)
decrypted_file.close()
