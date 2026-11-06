
# Division Algorithm

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

if b == 0:
    print("Division by zero is not allowed")
else:
    q = a // b
    r = a % b

    print("Quotient:", q)
    print("Remainder:", r)

    print("Verification:")
    print(a, "=", b, "*", q, "+", r)
