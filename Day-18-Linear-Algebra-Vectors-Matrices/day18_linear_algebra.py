import numpy as np

# Student features
student1 = np.array([5, 85, 78])
student2 = np.array([4, 90, 82])

# Add feature values
total = student1 + student2

# Difference
difference = student1 - student2

# Scale student 1
scaled = 2 * student1

print("Student 1:", student1)
print("Student 2:", student2)

print("\nAddition:", total)
print("Difference:", difference)
print("Scaled Student 1:", scaled)
