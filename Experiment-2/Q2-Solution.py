def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def generate_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")


n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Series:")
    generate_series(n)