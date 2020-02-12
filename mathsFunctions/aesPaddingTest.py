from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val = raw_input("Key ")
password = raw_input("Password ")

plain_text = val


def encrypt(plain_text, key, mode):
	enc_obj = AES.new(key,mode)
	return enc_obj.encrypt(plain_text)


def decrypt(cipher_text, key, mode):
	enc_obj = AES.new(key,mode)
	return(enc_obj.decrypt(cipher_text))


print "\nAES"
key = hashlib.sha256(password).digest()

plain_text = Padding.appendPadding(plain_text,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plain_text))

cipher_text = encrypt(plain_text,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(cipher_text))

plain_text = decrypt(cipher_text,key,AES.MODE_ECB)
plain_text = Padding.removePadding(plain_text,mode='CMS')
print "  decrypt: "+plain_text

plain_text = Padding.appendPadding(plain_text,blocksize=Padding.AES_blocksize,mode='Null')
print "After padding (Null): "+binascii.hexlify(bytearray(plain_text))

cipher_text = encrypt(plain_text,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(cipher_text))

plain_text = decrypt(cipher_text,key,AES.MODE_ECB)
plain_text = Padding.removePadding(plain_text,mode='Null')
print "  decrypt: "+plain_text

plain_text = Padding.appendPadding(plain_text,blocksize=Padding.AES_blocksize,mode='Space')
print "After padding (Space): "+binascii.hexlify(bytearray(plain_text))

cipher_text = encrypt(plain_text,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(cipher_text))

plain_text = decrypt(cipher_text,key,AES.MODE_ECB)
plain_text = Padding.removePadding(plain_text,mode='Space')
print "  decrypt: "+ plain_text