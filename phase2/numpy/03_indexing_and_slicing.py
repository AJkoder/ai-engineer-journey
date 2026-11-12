import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Elements from index 1 to 3:", arr[1:4])
print("Every second element:", arr[::2])

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nComplete array:")
print(data)

print("First row:", data[0, :])
print("Second column:", data[:, 1])
print("Element at row 1, column 2:", data[1, 2])
print("Selected section:")
print(data[0:2, 1:3])
