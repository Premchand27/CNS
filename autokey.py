class AutokeyCipher:
    def __init__(self, key):
        self.key = key.upper()

    def extend_key(self, message):
        extended_key = self.key
        for char in message.upper():
            if char.isalpha():
                extended_key += char
        return extended_key

    def encrypt(self, message):
        message = message.upper()
        extended_key = self.extend_key(message)
        ciphertext = ''
        for i in range(len(message)):
            if message[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                encrypted_char = chr((ord(message[i]) - ord('A') + shift) % 26 + ord('A'))
                ciphertext += encrypted_char
            else:
                ciphertext += message[i]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        extended_key = self.extend_key(ciphertext)
        plaintext = ''
        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
                plaintext += decrypted_char
            else:
                plaintext += ciphertext[i]
        return plaintext

if __name__ == "__main__":
    key = "KEY"
    cipher = AutokeyCipher(key)

    plaintext = input("Enter the plaintext: ")
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
