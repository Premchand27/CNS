class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?! '

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_index = (self.a * index + self.b) % len(self.alphabet)
                ciphertext += self.alphabet[encrypted_index]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        a_inv = self.mod_inverse(self.a, len(self.alphabet))
        for char in ciphertext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                decrypted_index = (a_inv * (index - self.b)) % len(self.alphabet)
                plaintext += self.alphabet[decrypted_index]
            else:
                plaintext += char
        return plaintext

    def mod_inverse(self, a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

if __name__ == "__main__":
    cipher = AffineCipher(3, 12)

    plaintext = input("Enter the plaintext: ")
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
