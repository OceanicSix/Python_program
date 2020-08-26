# You can import all modules you need from Crypto here
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

def compute_hash(msg):
    #TODO starts #
    hash_val = ''
    hash=SHA256.new()
    hash.update(msg)
    hash_val=hash.digest()
    #TODO ends  #
    return hash_val

def get_parameters():
    key_length = 2048
    # TODO starts #
    iv = ("1234"*4).encode('utf-8')

    #RSA keys
    key=RSA.generate(key_length)
    pubkey_object=key.publickey().exportKey("PEM")
    prikey_object=key.exportKey("PEM")

    RSA_pub = RSA.importKey(pubkey_object)
    RSA_prv = RSA.importKey(prikey_object)

    #AES
    ID="28408033"
    AES_key = (ID+(16-len(ID))*"0").encode("utf-8")  # Please use your student ID plus zero padding to make a 16 byte key
    # TODO ends #
    return iv, AES_key, RSA_pub, RSA_prv  # return initialization vector and RSA keys

def AES_enc(msg, iv, key, mode = 'CFB'):
    #TODO starts #
    if mode=="CFB":
        Mode=AES.MODE_CFB
    aes_encryption = AES.new(key,Mode,iv)
    ciphertext = aes_encryption.encrypt(msg)
    #TODO ends   #
    return ciphertext

def AES_dec(ciphertext,iv,  key):
    #TODO starts #
    aes_decryption=AES.new(key,AES.MODE_CFB,iv)

    plaintext = aes_decryption.decrypt(ciphertext)
    #TODO ends   #
    return plaintext

def RSA_enc(message, key_pub):
    #TODO starts #

    enc_text =  key_pub.encrypt(message,32)
    return enc_text
    #TODO ends   #

def RSA_dec(ciphertext, key_prv):
    #TODO starts #

    plaintext = key_prv.decrypt(ciphertext)
    return plaintext
    #TODO ends   #

# def main():
#     a="123"
#     print(compute_hash(a))

def main():

    message = b"I love Monash University"
    #Step 1  Generate Initialization Vector and RSA key pair 
    iv, AES_key, RSA_pub, RSA_prv = get_parameters()

    #Step 2  Compute Hash value # 
    hash_val = compute_hash(message)
    print("----------------------------------------------------------")
    print("The hash value for given input is:\n {}".format(hash_val))
 
    #Step 4  AES  # 
    ciphertext = AES_enc(message, iv, AES_key)
    plaintext = AES_dec(ciphertext, iv, AES_key)
    print("----------------------------------------------------------")
    print("The ciphertext after AES algorithm\n {}".format(ciphertext))
    print("The text recovered is:\n {}".format(plaintext))

    #Step 5  RSA Signature  # 
    #TODO
    signature= RSA_prv.sign(hash_val,32)
    verify_signature=RSA_pub.verify(compute_hash(plaintext),signature)

    print("----------------------------------------------------------")
    print("The result of signature verification is: "+str(verify_signature))
    return 0

if __name__ == '__main__':
    main()
