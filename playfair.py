class PlayfairCipher:
    def __init__(self, key):
        self.key = self.clean_key(key)
        self.matrix = self.generate_matrix()

    def clean_key(self, key):
        clean_key = ''
        for char in key:
            if char.isalpha() and char not in clean_key:
                clean_key += char
        return clean_key

    def generate_matrix(self):
        alphabet = 'abcdefghiklmnopqrstuvwxyz'
        matrix = []
        key = self.key + alphabet
        for char in key:
            if char not in matrix:
                matrix.append(char)
        matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_positions(self, letter):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == letter:
                    return i, j

    def encrypt_pair(self, pair):
        row1, col1 = self.find_positions(pair[0])
        row2, col2 = self.find_positions(pair[1])

        if row1 == row2:
            return self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            return self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
        else:
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def encrypt(self, plaintext):
        plaintext = plaintext.replace('j', 'i')
        plaintext = plaintext.replace('J', 'I')

        pairs = []
        for i in range(0, len(plaintext), 2):
            if i == len(plaintext) - 1:
                pairs.append(plaintext[i] + 'X')
            elif plaintext[i] == plaintext[i + 1]:
                pairs.append(plaintext[i] + 'X')
            else:
                pairs.append(plaintext[i:i + 2])

        ciphertext = ''
        for pair in pairs:
            encrypted_pair = self.encrypt_pair(pair.lower())
            ciphertext += encrypted_pair.upper()

        return ciphertext

if __name__ == "__main__":
    key = "ldrpl"
    cipher = PlayfairCipher(key)

    plaintext = input("Enter the plaintext: ")
    encrypted = cipher.encrypt(plaintext)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
