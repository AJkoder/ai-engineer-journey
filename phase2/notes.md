
cat > phase2/notes.md <<'EOF'
# Phase 2 — NumPy Revision Notes

# 1. NUMPY INTRODUCTION

**Definition:** NumPy (Numerical Python) is a Python library used for fast numerical calculations and working with multidimensional arrays.

**Main object:** `ndarray` (N-dimensional array).

**Import:**
```python
import numpy as np
```

**Why NumPy?**
- Faster numerical operations than ordinary Python loops.
- Performs operations on entire arrays.
- Supports mathematical, statistical and matrix calculations.
- Widely used in Machine Learning and Deep Learning.

**Python List vs NumPy Array:**
- List: `numbers * 2` repeats the list.
- Array: `numbers * 2` multiplies every element by 2.

---

# 2. ARRAYS AND DIMENSIONS

**Definition:** An array is a collection of elements arranged in one or more dimensions.

| Array | Meaning | Example shape |
|---|---|---|
| 1D | Single row of values | `(3,)` |
| 2D | Rows and columns | `(2, 3)` |
| 3D | Collection of 2D arrays | `(2, 2, 3)` |

**Important properties:**

| Property | Meaning |
|---|---|
| `arr.ndim` | Number of dimensions |
| `arr.shape` | Size of each dimension |
| `arr.size` | Total number of elements |
| `arr.dtype` | Data type of elements |

**Example:**
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.ndim   # 2
arr.shape  # (2, 3)
arr.size   # 6
arr.dtype  # Integer type
```

**Use cases:** Representing datasets, images, numerical features and model inputs.

---

# 3. ARRAY CREATION FUNCTIONS

| Function | Purpose | Example |
|---|---|---|
| `np.array()` | Create an array | `np.array([1, 2, 3])` |
| `np.zeros()` | Array of zeros | `np.zeros((2, 3))` |
| `np.ones()` | Array of ones | `np.ones((2, 3))` |
| `np.full()` | Fill with given value | `np.full((2, 3), 7)` |
| `np.arange()` | Generate a range | `np.arange(0, 10, 2)` |
| `np.linspace()` | Fixed number of evenly spaced values | `np.linspace(0, 1, 5)` |
| `np.eye()` | Identity matrix | `np.eye(3)` |
| `np.random.rand()` | Random values between 0 and 1 | `np.random.rand(2, 3)` |

**Important differences:**

- `arange(start, stop, step)` uses a step size; stop is excluded.
- `linspace(start, stop, num)` uses a fixed number of values; endpoints are included by default.
- `zeros()` fills with 0.
- `ones()` fills with 1.
- `full()` fills with a specified value.

**Use cases:** Initializing arrays, generating sample data and creating matrices.

---

# 4. INDEXING AND SLICING

**Indexing:** Accessing a particular array element.

**Slicing:** Extracting a portion of an array.

### 1D indexing

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]    # 10
arr[-1]   # 50
arr[2]    # 30
```

### Slicing syntax

```python
arr[start:stop:step]
```

| Expression | Meaning |
|---|---|
| `arr[1:4]` | Index 1 to 3 |
| `arr[:3]` | First three elements |
| `arr[2:]` | Index 2 to end |
| `arr[::2]` | Every second element |
| `arr[::-1]` | Reverse array |

### 2D indexing

```python
arr[row, column]
```

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

data[1, 2]     # 60
data[0, :]     # First row
data[:, 1]     # Second column
data[0:2, 1:3] # Selected section
```

**Important points:**
- Indexing starts from 0.
- Negative indexing counts from the end.
- Slice stop index is excluded.
- `:` selects all elements along that axis.

**Use cases:** Selecting dataset rows, columns and individual features.

---

# 5. RESHAPING, FLATTENING AND TRANSPOSE

### Reshape

**Definition:** Changes the shape of an array without changing its total number of elements.

```python
arr = np.arange(1, 13)

arr.reshape(3, 4)
arr.reshape(2, 6)
arr.reshape(3, -1)
```

**Important rules:**
- Total number of elements must remain the same.
- Only one dimension can be inferred using `-1`.

### Flatten

**Definition:** Converts a multidimensional array into a 1D array.

```python
arr.flatten()
```

### Transpose

**Definition:** Swaps rows and columns in a 2D array.

```python
arr.T
```

Example: Shape `(2, 3)` becomes `(3, 2)`.

### Axis

**Definition:** Specifies the direction along which an operation is performed.

```python
np.sum(data, axis=0)  # Column-wise result
np.sum(data, axis=1)  # Row-wise result
```

**Remember:**
- `axis=0`: Collapse rows; get one result per column.
- `axis=1`: Collapse columns; get one result per row.

**Use cases:** Changing dataset shapes, preparing model inputs and calculating row/column statistics.

---

# 6. BROADCASTING

**Definition:** Broadcasting allows NumPy to perform operations on arrays with different but compatible shapes.

### Example

```python
arr = np.array([10, 20, 30])

print(arr + 5)
# [15 25 35]
```

NumPy automatically applies the scalar to every element.

### Array broadcasting

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([10, 20, 30])

print(A + B)
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

### Broadcasting rules

Compare dimensions from right to left.

Two dimensions are compatible if:
1. They are equal, OR
2. One of them is 1.

Missing dimensions are treated as 1.

**Examples:**

| Shape A | Shape B | Compatible? |
|---|---|---|
| `(2, 3)` | `(3,)` | Yes |
| `(3, 1)` | `(1, 4)` | Yes |
| `(2, 3)` | `(2, 2)` | No |
| `(2, 3)` | `(1, 3)` | Yes |

**Use cases:** Adding values to dataset columns, normalization and efficient mathematical operations.

---

# 7. MATHEMATICAL OPERATIONS

NumPy performs mathematical operations element-wise by default.

```python
A = np.array([10, 20, 30])
B = np.array([1, 2, 3])
```

| Operation | Syntax | Purpose |
|---|---|---|
| Addition | `A + B` | Add elements |
| Subtraction | `A - B` | Subtract elements |
| Multiplication | `A * B` | Element-wise multiplication |
| Division | `A / B` | Divide elements |
| Square | `np.square(A)` | Square each element |
| Square root | `np.sqrt(A)` | Square root |
| Power | `np.power(A, 2)` | Raise elements to a power |
| Sum | `np.sum(A)` | Total sum |
| Minimum | `np.min(A)` | Smallest value |
| Maximum | `np.max(A)` | Largest value |

**Important:** `A * B` is element-wise multiplication, not matrix multiplication.

**Use cases:** Feature calculations, transformations and numerical preprocessing.

---

# 8. STATISTICAL OPERATIONS

Statistics helps us understand and summarize numerical data.

| Function | Meaning |
|---|---|
| `np.mean(arr)` | Average |
| `np.median(arr)` | Middle value after sorting |
| `np.std(arr)` | Standard deviation |
| `np.var(arr)` | Variance |
| `np.percentile(arr, 25)` | 25th percentile |
| `np.min(arr)` | Minimum |
| `np.max(arr)` | Maximum |

### Important concepts

**Mean:** Sum of values divided by the number of values.

**Median:** Middle value after sorting. Less affected by extreme outliers than the mean.

**Variance:** Measures the average squared deviation from the mean.

**Standard deviation:** Square root of variance. Measures how spread out values are.

**Percentile:** Indicates the value below which a given percentage of observations falls.

### ddof

```python
np.std(arr)           # Population standard deviation
np.std(arr, ddof=1)   # Sample standard deviation
```

- Default `ddof=0`: Population calculation.
- `ddof=1`: Sample calculation.

**Use cases:** Analysing ratings, understanding datasets, detecting unusual values and preprocessing ML data.

---

# 9. MATRIX OPERATIONS

**Matrix:** A rectangular arrangement of numbers in rows and columns.

### Matrix addition and subtraction

```python
A + B
A - B
```

Both matrices must have compatible shapes; for ordinary matrix addition and subtraction, their shapes must be equal.

### Element-wise multiplication

```python
A * B
```

Multiplies corresponding elements.

### Matrix multiplication

```python
A @ B
np.matmul(A, B)
np.dot(A, B)
```

For 2D matrices, `np.dot()` and `np.matmul()` perform matrix multiplication.

### Matrix multiplication rule

For:

```text
A = (m, n)
B = (n, p)
```

Result shape:

```text
(m, p)
```

The inner dimensions must match.

Example:

```text
(3, 2) @ (2, 5) = (3, 5)
```

### Transpose

```python
A.T
```

Swaps rows and columns.

### Identity matrix

```python
np.eye(3)
```

A square matrix with ones on the main diagonal and zeros elsewhere.

### Determinant

```python
np.linalg.det(A)
```

A scalar value calculated from a square matrix.

### Inverse

```python
np.linalg.inv(A)
```

Finds the inverse of a square, non-singular matrix.

**Important:** A matrix has an inverse only when its determinant is non-zero.

### Solve linear equations

```python
np.linalg.solve(A, b)
```

Solves a system of linear equations. Usually preferred over explicitly calculating the inverse when solving `Ax = b`.

**Use cases:** Linear algebra, transformations, neural networks and machine learning calculations.

---

# 10. COMMON MISTAKES AND IMPORTANT DIFFERENCES

| Common confusion | Correct understanding |
|---|---|
| `ndim` vs `shape` | Dimensions count vs dimension sizes |
| `size` vs `shape` | Total elements vs dimensions |
| `arange` vs `linspace` | Step size vs number of values |
| `*` vs `@` | Element-wise vs matrix multiplication |
| `axis=0` vs `axis=1` | Column results vs row results |
| `mean` vs `median` | Average vs middle value |
| `flatten()` vs `reshape()` | Convert to 1D vs change shape |
| `np.dot()` vs `np.matmul()` | Both do 2D matrix multiplication |

### Common errors

1. **Reshape error:** New shape does not contain the same total number of elements.
2. **Broadcasting error:** Array dimensions are incompatible.
3. **Matrix multiplication error:** Inner dimensions do not match.
4. **Inverse error:** Matrix is singular or not square.
5. **Index error:** Requested index is outside the array bounds.

---

# 11. NUMPY IN AI AND MACHINE LEARNING

| Application | How NumPy helps |
|---|---|
| Dataset handling | Stores numerical features |
| Data preprocessing | Scaling and transforming values |
| Statistics | Mean, median and standard deviation |
| Linear algebra | Matrix and vector calculations |
| Neural networks | Numerical operations on weights and data |
| Image processing | Represents images as multidimensional arrays |
| Model evaluation | Calculates numerical metrics |

**HeartTalk example:**

- Store user feedback ratings in an array.
- Calculate average helpfulness.
- Analyse response times.
- Identify unusually low ratings.
- Compare chatbot performance.

---

# 12. INTERVIEW QUESTIONS

**Q1. What is NumPy?**

NumPy is a Python library for efficient numerical computations and multidimensional array operations.

**Q2. What is an ndarray?**

The N-dimensional array object provided by NumPy.

**Q3. Difference between Python list and NumPy array?**

Lists are general-purpose collections. NumPy arrays support efficient numerical operations and vectorization.

**Q4. What is broadcasting?**

A feature that allows operations on compatible arrays with different shapes.

**Q5. What is the difference between `*` and `@`?**

`*` performs element-wise multiplication. `@` performs matrix multiplication.

**Q6. What does `reshape()` do?**

Changes an array's shape without changing its total number of elements.

**Q7. What is the difference between `axis=0` and `axis=1`?**

For a 2D array, axis 0 gives column-wise results; axis 1 gives row-wise results.

**Q8. What is the difference between mean and median?**

Mean is the arithmetic average. Median is the middle value after sorting.

**Q9. What is an identity matrix?**

A square matrix with ones on the main diagonal and zeros elsewhere.

**Q10. When does a matrix have an inverse?**

When it is square and its determinant is non-zero.

**Q11. What is the difference between `arange()` and `linspace()`?**

`arange()` uses a step size; `linspace()` generates a specified number of evenly spaced values.

**Q12. What is vectorization?**

Performing operations on entire arrays instead of manually looping over individual elements.

---

# 13. QUICK REVISION CHEATSHEET

```python
# Import
import numpy as np

# Create arrays
np.array([1, 2, 3])
np.zeros((2, 3))
np.ones((2, 3))
np.full((2, 3), 5)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
np.eye(3)

# Array properties
arr.ndim
arr.shape
arr.size
arr.dtype

# Indexing and slicing
arr[0]
arr[-1]
arr[1:4]
arr[::-1]

# Reshaping
arr.reshape(2, 3)
arr.flatten()
arr.T

# Broadcasting
arr + 5
A + B

# Mathematical operations
np.sum(arr)
np.min(arr)
np.max(arr)
np.square(arr)
np.sqrt(arr)
np.power(arr, 2)

# Statistics
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.percentile(arr, 25)

# Matrix operations
A + B
A - B
A * B
A @ B
A.T
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.solve(A, b)
```

---

# NUMPY COMPLETION CHECKLIST

- [ ] Understand NumPy arrays and dimensions.
- [ ] Practise array creation functions.
- [ ] Practise indexing and slicing.
- [ ] Understand reshaping and axes.
- [ ] Understand broadcasting rules.
- [ ] Practise mathematical operations.
- [ ] Practise statistical functions.
- [ ] Understand matrix operations.
- [ ] Complete NumPy practice exercises.
- [ ] Complete the HeartTalk mini-project.
- [ ] Revise interview questions.
EOF
