import numpy as np

# 1D array
one_d = np.array([10, 20, 30])

# 2D array
two_d = np.array([[1, 2, 3], [4, 5, 6]])

# 3D array
three_d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

for name, arr in [
    ("1D", one_d),
    ("2D", two_d),
    ("3D", three_d)
]:
    print(f"\n{name} array:")
    print(arr)
    print("Dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Total elements:", arr.size)
