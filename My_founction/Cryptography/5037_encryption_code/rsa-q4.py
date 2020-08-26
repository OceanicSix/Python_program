import random
from random import randint
import os

# greatest common factor
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# A fast and effient implementation of power mod 
# (https://helloacm.com/compute-powermod-abn/)
def powmod(a, b, n):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % n
        b //= 2
        a = a * a % n
    return r

#returns y  such that e * y == 1 modulo phi
#https://stackoverflow.com/questions/44044143/why-is-my-rsa-implementation-in-python-not-working
def invert(e, phi):
    a, b, u = 0, phi, 1
    while(e > 0):
        q = b // e
        e, a, b, u = b % e, u, e, a-q*u
    if (b == 1):
        return a % phi
    else:
        print("Must be coprime!")

# generate a key pair
def rsa_keygen(N):
    status = True
    p = random.getrandbits(N//2)
    q = random.getrandbits(N//2)
    e = 65537
    n =  p * q
    phi_n = ( p - 1) * ( q - 1)
    if gcd(e , phi_n) == 1:
        d = invert(e, phi_n )
    else :
        status = False
        d = -1
    return status , n , e , d

def main():
    _ , n , e , d = rsa_keygen(2048)

    print ( 'n ={}\n e ={}\n d ={}'.format (n ,e , d ))

    random.seed(a = os.urandom (512), version = 2)

    pin = randint(0,1000000 )

    print ('Secret PIN is {:06d}'.format (pin))

    c = powmod( pin , e , n )

    print ( 'Encrypted PIN is \n{} '.format(c))
    for i in range (0 ,1000000) :
        # TODO starts
        test_result=powmod(i,e,n)
        if test_result==c:
            print("user pin is: "+str(i))


        # TODO ends
if __name__ == '__main__':
    main()
