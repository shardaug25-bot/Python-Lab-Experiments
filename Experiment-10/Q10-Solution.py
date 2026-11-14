# Experiment 10: Matrix Operations

import numpy as np


# Function to take matrix input
def input_matrix(rows, cols, name):
    matrix = []

    print("\nEnter elements of", name)

    for i in range(rows):
        row = list(map(int, input(
            f"Enter row {i + 1}: "
        ).split()))

        if len(row) != cols:
            print("Incorrect number of elements.")
            exit()

        matrix.append(row)

    return matrix


# Take dimensions
r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))


# Take matrix elements
A = input_matrix(r1, c1, "Matrix A")
B = input_matrix(r2, c2, "Matrix B")


# Without NumPy
print("\n========== WITHOUT NUMPY ==========")

# Addition and subtraction
if r1 == r2 and c1 == c2:

    addition = [
        [A[i][j] + B[i][j] for j in range(c1)]
        for i in range(r1)
    ]

    subtraction = [
        [A[i][j] - B[i][j] for j in range(c1)]
        for i in range(r1)
    ]

    print("\nAddition:")
    for row in addition:
        print(row)

    print("\nSubtraction:")
    for row in subtraction:
        print(row)

else:
    print("\nAddition and subtraction are not possible.")


# Multiplication
if c1 == r2:

    multiplication = [
        [
            sum(A[i][k] * B[k][j] for k in range(c1))
            for j in range(c2)
        ]
        for i in range(r1)
    ]

    print("\nMultiplication:")
    for row in multiplication:
        print(row)

else:
    print("\nMultiplication is not possible.")


# Transpose of A
transpose = [
    [A[i][j] for i in range(r1)]
    for j in range(c1)
]

print("\nTranspose of Matrix A:")
for row in transpose:
    print(row)


# With NumPy
print("\n========== WITH NUMPY ==========")

a = np.array(A)
b = np.array(B)

if a.shape == b.shape:
    print("\nAddition:")
    print(np.add(a, b))

    print("\nSubtraction:")
    print(np.subtract(a, b))
else:
    print("\nAddition and subtraction are not possible.")


if a.shape[1] == b.shape[0]:
    print("\nMultiplication:")
    print(np.matmul(a, b))
else:
    print("\nMultiplication is not possible.")


print("\nTranspose of Matrix A:")
print(np.transpose(a))