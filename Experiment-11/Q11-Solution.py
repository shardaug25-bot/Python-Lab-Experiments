# Experiment 11: Determinant, Inverse and Rank

import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

if rows != cols:
    print("Matrix must be square.")
    exit()

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = list(map(float, input().split()))

    if len(row) != cols:
        print("Invalid number of elements.")
        exit()

    matrix.append(row)

A = np.array(matrix)

# Calculate determinant
det = np.linalg.det(A)

print("\nMatrix:")
print(A)

print("\nDeterminant:", round(det, 2))

# Calculate inverse
if not np.isclose(det, 0):
    inverse = np.linalg.inv(A)
    print("\nInverse:")
    print(inverse)
else:
    print("\nInverse does not exist.")

# Calculate rank
rank = np.linalg.matrix_rank(A)

print("\nRank:", rank)