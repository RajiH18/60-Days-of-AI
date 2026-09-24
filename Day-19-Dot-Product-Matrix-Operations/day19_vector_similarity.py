import numpy as np

# Two vectors
A = np.array([1, 2, 3])
B = np.array([2, 4, 6])

# Dot product
dot_product = np.dot(A, B)

# Magnitudes
magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

# Cosine similarity
cosine_similarity = dot_product / (magnitude_A * magnitude_B)

print("Vector A:", A)
print("Vector B:", B)

print("Dot Product:", dot_product)
print("Magnitude of A:", magnitude_A)
print("Magnitude of B:", magnitude_B)

print("Cosine Similarity:", round(cosine_similarity, 4))