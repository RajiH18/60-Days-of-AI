import numpy as np

# Create a 2D NumPy array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Number of dimensions
print("Number of dimensions:", matrix.ndim)

# Shape of the array
print("Shape:", matrix.shape)

# Access elements using indexing
print("Element at [1, 1]:", matrix[1, 1])
print("Element at [2, 2]:", matrix[2, 2])