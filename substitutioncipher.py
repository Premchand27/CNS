class SubstitutionCipher:
    def __init__(self, key='defghijklmnopqrstuvwxyzabc'):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if len(key) != len(self.alphabet):
            raise ValueError("Key length must be equal to alphabet length")
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext.lower():
            if char.isalpha():
                index = self.alphabet.index(char)
                ciphertext += self.key[index].upper() if char.isupper() else self.key[index]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext.lower():
            if char.isalpha():
                index = self.key.index(char)
                plaintext += self.alphabet[index].upper() if char.isupper() else self.alphabet[index]
            else:
                plaintext += char
        return plaintext

if __name__ == "__main__":
    cipher = SubstitutionCipher()
    plaintext = input("Enter the plaintext: ")

    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
