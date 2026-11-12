import numpy as np

# Scalar broadcasting
arr = np.array([10, 20, 30])
print("Array + 5:", arr + 5)

# Compatible shapes: (2, 3) and (3,)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
values = np.array([10, 20, 30])

print("\nMatrix:")
print(matrix)
print("Values:", values)
print("Broadcasting result:")
print(matrix + values)

# Broadcasting compares dimensions from right to left.
# Dimensions must be equal or one of them must be 1.
