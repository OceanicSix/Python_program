from Crypto.Cipher import AES
from Crypto.Hash import MD5  # MD5 can generate 32byte long key, sha256 will generate 64byte not suit for AES
import base64


class AES_encryption:
    def __init__(self, password, block_size=32, padding="{"):
        # create key and cipher
        key = MD5.new()
        key.update(password.encode("utf-8"))  # convert password from "str" to "byte" type
        self.cipher = AES.new(key.hexdigest())

        self.block_size = block_size
        self.padding = padding

    def encrypt(self, message):
        message = message + (self.block_size - len(message) % self.block_size) * self.padding
        encrypted_message = self.cipher.encrypt(message)
        ciphertext = base64.b64encode(encrypted_message)
        return ciphertext

    def decrypt(self, ciphertext):
        encrypted_message = base64.b64decode(ciphertext)
        message = self.cipher.decrypt(encrypted_message).decode("utf-8").rstrip(self.padding)  # convert message
        # from "byte" to "str"
        return message


if __name__ == '__main__':
    a_encryption = AES_encryption("89757")
    ciphertext = a_encryption.encrypt("abcdefg")
    print(ciphertext)
    print(a_encryption.decrypt(ciphertext))
