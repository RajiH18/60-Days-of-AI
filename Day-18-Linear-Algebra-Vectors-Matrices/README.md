# 📐 Day 18 — Linear Algebra: Vectors & Matrices

## 🎯 Topic

**Linear Algebra — Vectors & Matrices**

Today I started learning **Linear Algebra** as part of **Week 3: Mathematics for AI** in my 60-Day AI Learning Journey.

## 📚 What I Learned

- What is Linear Algebra?
- What is a Vector?
- Vector dimensions
- Vector addition
- Vector subtraction
- Scalar multiplication
- What is a Matrix?
- Matrix dimensions and shape
- Matrix addition
- Matrix multiplication
- Basic NumPy operations
- Why vectors and matrices are important in AI and Machine Learning

## 🔢 Vectors

A vector is an ordered collection of numbers.

Example:

```text
[10, 20, 30]
```

This is a **3-dimensional vector** with shape:

```text
(3,)
```

In AI, student information can be represented as a vector:

```text
[Study Hours, Attendance, Marks]

[5, 85, 78]
```

## ➕ Vector Operations

### Vector Addition

```text
A = [1, 2, 3]
B = [4, 5, 6]

A + B = [5, 7, 9]
```

### Vector Subtraction

```text
A = [5, 7, 9]
B = [1, 2, 3]

A - B = [4, 5, 6]
```

### Scalar Multiplication

```text
A = [2, 4, 6]

3 × A = [6, 12, 18]
```

## 🧮 Matrices

A matrix is a rectangular arrangement of numbers in rows and columns.

Example:

```text
[1 2 3]
[4 5 6]
```

This matrix has:

- 2 rows
- 3 columns
- Shape = `(2, 3)`

## ➕ Matrix Addition

```text
A = [1 2]      B = [5 6]
    [3 4]          [7 8]

A + B = [6  8]
        [10 12]
```

## ✖️ Matrix Multiplication

Matrix multiplication uses the **row × column** operation.

```text
A = [1 2]      B = [5 6]
    [3 4]          [7 8]

A × B = [19 22]
        [43 50]
```

In NumPy:

```python
result = A @ B
```

## 🐍 Python with NumPy

I practiced vector and matrix operations using **NumPy**.

```python
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Scalar multiplication:", 3 * A)
```

## 🛠️ Mini Project

### Student Feature Calculator

I created a simple Python program using NumPy to perform operations on student features.

```text
Student 1 = [5, 85, 78]
Student 2 = [4, 90, 82]
```

The program performs:

- Vector addition
- Vector subtraction
- Scalar multiplication

## 🤖 Why Vectors & Matrices Matter in AI

Machine Learning models work with numerical data.

A simplified view is:

```text
Data
  ↓
Vectors
  ↓
Matrices
  ↓
Mathematical Operations
  ↓
Prediction
```

Vectors and matrices are important building blocks of many Machine Learning and Deep Learning algorithms.

## 💭 Challenge I Faced

Matrix multiplication was a little confusing at first because it is different from normal element-by-element multiplication.

After practicing the **row × column** method and using NumPy, I understood it better.

## 💡 Key Takeaway

> **Vectors and matrices are not just mathematical concepts. They are used to represent data and perform calculations in AI and Machine Learning.**

## 🚀 Progress

**Day 18 completed ✅**

**18 days completed | 42 days to go**

Still learning, practicing, and understanding one concept at a time. 🌱💻