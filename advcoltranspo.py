def generate_key(keyword):
    key = "".join(dict.fromkeys(keyword))
    sorted_key = sorted(key)
    return "".join(sorted_key)

def encrypt(message, keyword):
    key = generate_key(keyword)
    key_indices = {char: index for index, char in enumerate(key)}
    num_columns = len(key)
    num_rows = -(-len(message) // num_columns)

    matrix = [[""] * num_columns for _ in range(num_rows)]

    for i, char in enumerate(message):
        row = i // num_columns
        col = i % num_columns
        matrix[row][key_indices[key[col]]] = char

    ciphertext = ""
    for col in range(num_columns):
        for row in range(num_rows):
            ciphertext += matrix[row][col]

    return ciphertext

def decrypt(ciphertext, keyword):
    key = generate_key(keyword)
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)
    last_col_chars = len(ciphertext) % num_columns
    col_chars = [num_rows - 1 + (1 if col < last_col_chars else 0) for col in range(num_columns)]
    ignore_chars = [sum(col_chars[:col]) for col in range(num_columns)]
    matrix = [[""] * num_columns for _ in range(num_rows)]

    for col, char_count in enumerate(col_chars):
        for row in range(char_count):
            index = ignore_chars[col] + row
            matrix[row][col] = ciphertext[index]

    plaintext = ""
    for row in range(num_rows):
        for col in range(num_columns):
            plaintext += matrix[row][key.index(sorted(key)[col])]

    return plaintext

# Take user input for keyword and message
keyword = input("Enter the keyword: ").upper()
message = input("Enter the message: ")

encrypted_message = encrypt(message, keyword)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, keyword)
print("Decrypted message:", decrypted_message)
