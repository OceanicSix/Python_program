from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
#
# # a="123".encode("utf-8")
# # hash=SHA256.new()
# # hash.update(a)
# # value=hash.digest()
# # print(123)
# # print(value)
# #
# # hash_object = SHA256.new(data=b'123')
# # value2=hash_object.digest()
# # print(value2)
#
key=RSA.generate(2048)
pub_key_object=key.publickey().exportKey("PEM")

serect_key_object=key.exportKey("PEM")
print("\n"+"\n")


ct=RSA.importKey(pub_key_object).encrypt("123".encode("utf-8"),31)
print(ct)

pt=RSA.importKey(serect_key_object).decrypt(ct)
print(pt)

# ID="28408033"
# AES_key = (ID+(16-len(ID))*"0").encode("utf-8")
# iv = ("1234"*4).encode('utf-8')
#
#
# pt="1234567890123456".encode("utf-8")
# print("pt is: ")
# print(pt)
# aes_object=AES.new(AES_key,AES.MODE_CFB,iv)
# ciphertext=aes_object.encrypt(pt)
#
#
#
# original_mes=aes_object.decrypt(ciphertext)
# print("original_mes is: ")
# print(original_mes)