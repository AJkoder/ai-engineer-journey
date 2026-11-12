import numpy as np

# NumPy is a Python library used for fast numerical calculations.

python_list = [10, 20, 30, 40]
numpy_array = np.array(python_list)

print("Python list:", python_list)
print("NumPy array:", numpy_array)
print("Array type:", type(numpy_array))
print("Array data type:", numpy_array.dtype)

# NumPy performs operations on all elements at once.
print("Array multiplied by 2:", numpy_array * 2)
