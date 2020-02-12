from Crypto.Cipher import DES
import hashlib
import Padding
import binascii

password = raw_input("Enter key")
cipher_text = raw_input("Enter cipher")


def decrypt(cipher_text, key, mode):
    enc_obj = DES.new(key, mode)
    return enc_obj.decrypt(cipher_text)


key = hashlib.sha256(password).digest()[:8]
cipher_text = binascii.unhexlify(cipher_text)
plain_text = decrypt(cipher_text, key, DES.MODE_ECB)
plain_text = Padding.removePadding(plain_text, mode='CMS')

print "  decrypt: " + plain_text