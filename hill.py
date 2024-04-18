import numpy as np

key_matrix = np.array([[17, 17, 5],
                       [21, 18, 21],
                       [2, 2, 19]])

def hill_encrypt(message, key_matrix):
   
    message_numbers = [ord(char) - ord('A') for char in message]

   
    while len(message_numbers) % key_matrix.shape[0] != 0:
        message_numbers.append(23)  

    
    message_matrix = np.array(message_numbers).reshape(-1, key_matrix.shape[0])

  
    encrypted_matrix = np.dot(message_matrix, key_matrix) % 26

  
    encrypted_message = ''
    for row in encrypted_matrix:
        for num in row:
            encrypted_message += chr(num + ord('A'))
    return encrypted_message

message = "PAY"

encrypted_message = hill_encrypt(message, key_matrix)
print("Encrypted message:", encrypted_message)
