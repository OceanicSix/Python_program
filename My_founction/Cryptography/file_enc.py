import argparse, os, sys

from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Protocol.KDF import PBKDF2

# check arguments
parser = argparse.ArgumentParser()
parser.add_argument("file", help="the file we want to encrypt/decrypt")
parser.add_argument("key", help="your key")
parser.add_argument("-e", "--encrypt", action="store_true")
parser.add_argument("-d", "--decrypt", action="store_true")
args = parser.parse_args()

# input file
try:
    inputfile = open(args.file, "rb")
except IOError:
    sys.exit("Could not open the input file")

# output file
try:
    output = open("a.out", "wb")
except IOError:
    sys.exit("Could not create the output file")

# make 256bits keys for encryption and mac
salt = "this is a salt"
kdf = PBKDF2(args.key, salt, 64, 1000)
key = kdf[:32]
key_mac = kdf[32:]

# create HMAC
mac = HMAC.new(key_mac)  # default is MD5

# encryption
if args.encrypt:
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)

    encrypted = cipher.encrypt(inputfile.read())
    mac.update(iv + encrypted)

    # output
    output.write(mac.hexdigest())
    output.write(iv)
    output.write(encrypted)

# decryption
else:
    data = inputfile.read()
    # check for MAC first
    verify = data[0:32]
    mac.update(data[32:])

    if mac.hexdigest() != verify:
        sys.exit("message was modified, aborting decryption")

    # decrypt
    iv = data[32:48]
    cipher = AES.new(key, AES.MODE_CFB, iv)

    decrypted = cipher.decrypt(data[48:])

    # output
    output.write(decrypted)