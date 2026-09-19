import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Ravi", "Anu", "Priya", "Kiran", "Sneha"],
    "Python": [78, 92, 65, 88, 75],
    "Java": [70, 89, 60, 85, 80],
    "SQL": [82, 95, 68, 90, 77]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Calculate average marks
df["Average"] = df[["Python", "Java", "SQL"]].mean(axis=1)

print("\nStudent Average:")
print(df[["Name", "Average"]])

# Find highest scorer
highest = df.loc[df["Average"].idxmax()]

print("\nHighest Scorer:")
print(highest)

# Create bar chart
plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")

plt.show()