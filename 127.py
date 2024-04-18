def bitwise_and_with_127(string):
    result = ""
    for char in string:
        result += chr(ord(char) & 127)
    return result

char_pointer = "Hello world"
result = bitwise_and_with_127(char_pointer)
print("Result of bitwise AND operation with each character using value 127:")
print(result)
