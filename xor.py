def main():
    str = "Hello World"
    str1 = ""

    for char in str:
        str1 += chr(ord(char) ^ 0)

    print(str1)

if __name__ == "__main__":
    main()
