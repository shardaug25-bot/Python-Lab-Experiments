n = int(input("Enter a number: "))

# Factorial
fact = 1

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)

# Prime number
if n <= 1:
    print(n, "is not a prime number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")