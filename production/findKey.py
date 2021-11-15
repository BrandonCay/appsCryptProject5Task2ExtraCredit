import binascii
from Crypto.Cipher import AES   


def findKey():
    with open('./keys.txt') as fp:
        keys=fp.readlines()
    
    iv=binascii.unhexlify('09080706050403020100A2B2C2D2E2F2'.lower()) 
    plaintext=binascii.unhexlify('255044462d312e350a25d0d4c5d80a34'.lower())  
    ciphertext=binascii.unhexlify('d06bf9d0dab8e8ef880660d2af65aa82'.lower())

    for keyhex in keys:
        keyhex=keyhex.rstrip()

        key=binascii.unhexlify(keyhex.lower()) 

        encryptor=AES.new(key, AES.MODE_CBC, iv)
        ciphertextAttempt=encryptor.encrypt(plaintext)

        if(ciphertextAttempt==ciphertext): 
            print ('iv: ', binascii.hexlify(iv))
            print ('plaintext: ', binascii.hexlify(plaintext))
            print ('key: ', binascii.hexlify(key))
            print ('ciphertext: ', binascii.hexlify(ciphertextAttempt))
