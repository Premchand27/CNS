class AdvancedColumnarTransposition:
    def __init__(self, key):
        self.key = key.upper()
        self.key_order = sorted(range(len(self.key)), key=lambda k: self.key[k])

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "").upper()
        num_columns = len(self.key)
        num_rows = (len(plaintext) + num_columns - 1) // num_columns
        plaintext += '*' * (num_rows * num_columns - len(plaintext))
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        plaintext_index = 0
        for col in range(num_columns):
            for row in range(num_rows):
                matrix[row][self.key_order[col]] = plaintext[plaintext_index]
                plaintext_index += 1
        encrypted_text = ''
        for col in range(num_columns):
            for row in range(num_rows):
                encrypted_text += matrix[row][col]
        return encrypted_text

    def decrypt(self, ciphertext):
        num_columns = len(self.key)
        num_rows = len(ciphertext) // num_columns
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        col_lengths = [len(ciphertext) // num_columns] * num_columns
        for i in range(len(ciphertext) % num_columns):
            col_lengths[i] += 1
        text_index = 0
        for col in range(num_columns):
            for row in range(num_rows):
                matrix[row][col] = ciphertext[text_index:text_index + col_lengths[col]]
                text_index += col_lengths[col]
        plaintext = ''
        for row in range(num_rows):
            for col in self.key_order:
                plaintext += matrix[row][col]
        return plaintext.rstrip('*')

if __name__ == "__main__":
    key = input("Enter the columnar transposition key: ")
    cipher = AdvancedColumnarTransposition(key)

    plaintext = input("Enter the plaintext: ")
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
