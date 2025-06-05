from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_message(message, key):  # key is already bytes
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = binascii.hexlify(cipher.iv).decode()
    ct = binascii.hexlify(ct_bytes).decode()
    return iv + ct

def decrypt_message(ciphertext_hex, key):  # key is already bytes
    iv = bytes.fromhex(ciphertext_hex[:32])
    ct = bytes.fromhex(ciphertext_hex[32:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()
