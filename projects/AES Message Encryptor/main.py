import hashlib
from utils import encrypt_message, decrypt_message

print("AES Message Encryptor")
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
raw_key = input("Enter passphrase: ").strip()
key = hashlib.sha256(raw_key.encode()).digest()[:16]  # AES-128

if mode == "encrypt":
    message = input("Enter message to encrypt: ")
    ciphertext = encrypt_message(message, key)
    print(f"Encrypted: {ciphertext}")

elif mode == "decrypt":
    ciphertext = input("Enter message to decrypt (hex): ")
    try:
        plaintext = decrypt_message(ciphertext, key)
        print(f"Decrypted: {plaintext}")
    except:
        print("Decryption failed. Wrong key or data.")
