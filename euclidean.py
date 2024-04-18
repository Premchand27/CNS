def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Take user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD using Euclidean Algorithm
gcd = euclidean_algorithm(num1, num2)

# Output the result
print("The GCD of", num1, "and", num2, "is:", gcd)
