
# Fermat's Little Theorem

a = int(input("Enter a: "))
p = int(input("Enter prime number p: "))

if p <= 1:
    print("p must be greater than 1")
else:
    # Check whether p is prime
    is_prime = True

    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            is_prime = False
            break

    if not is_prime:
        print("p is not prime")
    elif a % p == 0:
        print("a and p are not coprime")
    else:
        result = pow(a, p - 1, p)
        print("a^(p-1) mod p =", result)

        if result == 1:
            print("Fermat's Little Theorem is verified")
