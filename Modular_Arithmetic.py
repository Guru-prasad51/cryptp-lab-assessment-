
# Modular Arithmetic

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
n = int(input("Enter modulus: "))

if n <= 0:
    print("Modulus must be positive")
else:
    print("Addition:", (a + b) % n)
    print("Subtraction:", (a - b) % n)
    print("Multiplication:", (a * b) % n)
    print("Power:", pow(a, b, n))
