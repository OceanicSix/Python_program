from Crypto.Cipher import AES
import base64
import os # to use urandom to generate key


def encryption(msg):
    BLOCK_SIZE = 16  # 128 bits pt and key
    PADDING = "{"

    pad = lambda m: m + (BLOCK_SIZE - len(m) % BLOCK_SIZE) * PADDING # add padding
    encode_method= lambda c,m: base64.b64encode(c.encrypt(pad(m)))

    key=os.urandom(BLOCK_SIZE)
    print(key)


    cipher =AES.new(key)
    cipher_text =encode_method(cipher,msg)
    print(type(cipher_text))
    print(cipher_text)


    decode_method = lambda c, ct: c.decrypt(base64.b64decode(ct)).rstrip(PADDING)
    original_msg = decode_method(cipher, cipher_text)
    print(original_msg)

# def decryption(cipher_text):
#     PADDINg ="{"
#     decode_method=lambda c,ct:c.decrypt(base64.b64decode(ct).rstrip(PADDINg))
#     key='"yw/q\xd7x5\xca\x12\xaf_\xc7WP\xb5'
#     cipher=AES.new(key)
#     msg=decode_method(cipher,cipher_text)
#     print(msg)

encryption("abc")
#decryption('5R8xLGnGRYvEmkIr+EOl/Q==')
