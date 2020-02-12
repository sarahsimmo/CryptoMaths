from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val = raw_input("Key ")
password = raw_input("Password ")

plain_text = val


def encrypt(plain_text, key, mode):
	enc_obj = DES.new(key,mode)
	return enc_obj.encrypt(plain_text)


def decrypt(cipher_text, key, mode):
	enc_obj = DES.new(key,mode)
	return(enc_obj.decrypt(cipher_text))


print "\nDES"
key = hashlib.sha256(password).digest()[:8]


def text_pad(text, pad_mode):
	return Padding.appendPadding(text, blocksize=Padding.DES_blocksize, mode=pad_mode)


plain_text = text_pad(plain_text, 'CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plain_text))

cipher_text = encrypt(plain_text,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(cipher_text))

plain_text = decrypt(cipher_text,key,DES.MODE_ECB)
plain_text = Padding.removePadding(plain_text,mode='CMS')
print "  decrypt: "+plain_text

plain_text = text_pad(plain_text, 'Null')
print "After padding (Null): "+binascii.hexlify(bytearray(plain_text))

cipher_text = encrypt(plain_text,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(cipher_text))

plain_text = decrypt(cipher_text,key,DES.MODE_ECB)
plain_text = Padding.removePadding(plain_text,mode='Null')
print "  decrypt: "+plain_text

plain_text = text_pad(plain_text, 'Space')
print "After padding (Space): "+binascii.hexlify(bytearray(plain_text))

cipher_text = encrypt(plain_text,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(cipher_text))

plain_text = decrypt(cipher_text,key,DES.MODE_ECB)
plain_text = Padding.removePadding(plain_text,mode='Space')
print "  decrypt: "+ plain_text