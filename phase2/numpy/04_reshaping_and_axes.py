import numpy as np

arr = np.arange(1, 13)

print("Original:", arr)
print("Reshaped to 3x4:")
print(arr.reshape(3, 4))

print("\nReshaped with inferred dimension:")
print(arr.reshape(2, -1))

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nOriginal 2D array:")
print(data)

print("Flattened:", data.flatten())
print("Transpose:")
print(data.T)

# axis=0: calculate down the rows, giving column results.
print("Column sums:", np.sum(data, axis=0))

# axis=1: calculate across columns, giving row results.
print("Row sums:", np.sum(data, axis=1))
