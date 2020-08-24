
#import libraries
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util import Counter
from Crypto import Random
from binascii import hexlify

#this is only used for CTR mode
# Set up the counter with a nonce and initial value.
ctr_iv = int(hexlify(Random.new().read(AES.block_size)), 16)
#print('CTR IV (int): {0}'.format(ctr_iv))
ctr_encrypt_counter = Counter.new(128, initial_value=ctr_iv)
ctr_decrypt_counter = Counter.new(128, initial_value=ctr_iv)

def _pad_str(s, bs=32):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def _unpad_str(s):
        return s[:-ord(s[len(s)-1:])]
    
    
def encryption(key, raw, iv, mode):
    if mode != AES.MODE_CTR:
        cipher = AES.new(key,mode,iv)
    else:
        cipher = AES.new(key,AES.MODE_CTR,counter=ctr_encrypt_counter)
        
    return cipher.encrypt(raw)

def decryption(key, ctext,iv,mode):
    if mode != AES.MODE_CTR:       
        cipher = AES.new(key,mode,iv)
    else:
        cipher = AES.new(key,AES.MODE_CTR,counter=ctr_decrypt_counter)
        
    return cipher.decrypt(ctext)  
   
#generate 128bits-16 bytes key and iv
k = ("Network Security").encode('utf-8')
iv = ("1234"*4).encode('utf-8')

#plaintext is a character string of 5 blocks of 16 bytes 
plaintext = "Monash_FIT3031**"*5

print("Plaintext")
print(plaintext)

ciphertext= encryption(k,plaintext,iv,AES.MODE_ECB)

print("Ciphertext in hex mode")
print(ciphertext)

content= decryption(k,ciphertext,iv,AES.MODE_ECB).decode("utf-8")
print("Content after decryption")
print(content)
