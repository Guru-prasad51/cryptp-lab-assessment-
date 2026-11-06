
# Euler's Totient Function

n = int(input("Enter a number: "))

if n <= 0:
    print("Enter a positive integer")
else:
    count = 0

    for i in range(1, n + 1):
        a, b = i, n

        while b != 0:
            a, b = b, a % b

        if a == 1:
            count += 1

    print("Euler's Totient =", count)
