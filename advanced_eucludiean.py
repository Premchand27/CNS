def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        gcd, x, y = extended_euclidean_algorithm(num1, num2)
        print("The GCD of", num1, "and", num2, "is:", gcd)
        print("Coefficients (x, y) satisfying ax + by = gcd are:", x, ",", y)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
