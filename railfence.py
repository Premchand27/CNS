def encrypt_rail_fence(text, rails):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail][0] += char
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    cipher_text = ''
    for row in fence:
        cipher_text += ''.join(row)

    return cipher_text

def decrypt_rail_fence(cipher_text, rails):
    fence = [['' for _ in range(len(cipher_text))] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in cipher_text:
        fence[rail][0] = '*'
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*':
                fence[i][j] = cipher_text[index]
                index += 1

    rail = 0
    direction = 1
    plain_text = ''
    for _ in range(len(cipher_text)):
        plain_text += fence[rail][0]
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    return plain_text.replace('*', '')

# Example usage:
plaintext = input("Enter the plain text:")
rails = int(input("Enter the no of rails::"))

# Encryption
encrypted_text = encrypt_rail_fence(plaintext, rails)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted:", decrypted_text)
