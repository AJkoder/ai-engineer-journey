import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition:")
print(A + B)

print("\nSubtraction:")
print(A - B)

# Element-wise multiplication
print("\nElement-wise multiplication:")
print(A * B)

# Matrix multiplication
print("\nMatrix multiplication:")
print(A @ B)

# Transpose
print("\nTranspose of A:")
print(A.T)

# Identity matrix
print("\nIdentity matrix:")
print(np.eye(2))

# Determinant
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Inverse
print("\nInverse of A:")
print(np.linalg.inv(A))

# Matrix multiplication shape example:
# (3, 2) @ (2, 5) produces shape (3, 5).
