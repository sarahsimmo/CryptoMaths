from Crypto.Cipher import AES
import hashlib
import Padding
import binascii
import base64

password = raw_input("Enter key")
cipher_text = raw_input("Enter cipher")
password_list = ["hello", "ankle", "changeme", "123456"]

encoding = str
while encoding != 'base64' and encoding != 'hex':
    encoding = raw_input("Enter type (base64 or hex) ")
    b64 = False
    if encoding == 'base64':
        b64 = True



def decrypt(cipher_text, key, mode):
    enc_obj = AES.new(key, mode)
    return enc_obj.decrypt(cipher_text)


def set_key(password):
    return hashlib.sha256(password).digest()


def try_next_key(current_key):
    for pindex in range(len(password_list)):
        if password_list[pindex] == current_key:
                if not(pindex + 1 > len(password_list)):
                  return password_list[pindex + 1]
                else:
                    print("no valid passwords")
                    return None


def crack(password, cipher_text):
    key = set_key(password)
    plain_text = decrypt(cipher_text, key, AES.MODE_ECB)
    try:
        plain_text = Padding.removePadding(plain_text, mode='CMS')
        print "  decrypt: " + plain_text
    except AssertionError:
        password = try_next_key(password)
        if password is not None:
            crack(password, cipher_text)


if password == '':
    password = password_list[0]

if b64:
    cipher_text = base64.decodestring(cipher_text).encode('hex')

cipher_text = binascii.unhexlify(cipher_text)
crack(password, cipher_text)

