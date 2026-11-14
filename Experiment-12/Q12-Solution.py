# Experiment 12: Eigenvalues and Eigenvectors

import numpy as np

n = int(input("Enter order of square matrix: "))

matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = list(map(float, input().split()))

    if len(row) != n:
        print("Invalid number of elements.")
        exit()

    matrix.append(row)

A = np.array(matrix)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nMatrix:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)