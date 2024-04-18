def caesar_cipher(text, shift):
    """
    Encrypts/Decrypts the given text using Caesar Cipher with the specified shift.
    
    Args:
    - text (str): The text to be encrypted/decrypted.
    - shift (int): The number of positions to shift the letters (positive for encryption, negative for decryption).
    
    Returns:
    - str: The encrypted/decrypted text.
    """
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

# Example usage:
plaintext = input("Enter the plaintext: ")
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)
