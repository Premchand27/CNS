from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Use ECB mode for simplicity, but it's not recommended for general use.
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

def main():
    key = get_random_bytes(16)  # 16 bytes key for AES-128

    # Get plaintext from user input
    plaintext = input("Enter the text you want to encrypt: ").encode("utf-8")

    # Encryption
    encrypted = aes_encrypt(plaintext, key)
    print("Encrypted:", encrypted)

    # Decryption
    decrypted = aes_decrypt(encrypted, key)
    print("Decrypted:", decrypted.decode("utf-8"))

if __name__ == "__main__":
    main()
