
# Relative Prime Check

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y != 0:
    x, y = y, x % y

if x == 1:
    print(a, "and", b, "are relatively prime")
else:
    print(a, "and", b, "are not relatively prime")

print("GCD =", abs(x))
