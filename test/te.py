import base64
#from Crypto.Hash import MD5
from Crypto.Hash import SHA512
password="89757"
secret = SHA512.new()
secret.update(password.encode('utf-8'))
hash=secret.hexdigest()
print(hash)
print(len(hash))