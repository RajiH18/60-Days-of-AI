import pandas as pd

# Series
marks = pd.Series([80, 90, 70, 85])

print("Series:")
print(marks)

# Creating a DataFrame
data = {
    "Name": ["Raji", "Anu", "Kiran", "Rahul"],
    "Marks": [85, 92, 76, 88],
    "Age": [21, 20, 22, 21]
}

df = pd.DataFrame(data)

print("\nComplete DataFrame:")
print(df)

# Accessing columns
print("\nName column:")
print(df["Name"])

print("\nMarks column:")
print(df["Marks"])

# Multiple columns
print("\nName and Marks:")
print(df[["Name", "Marks"]])

# DataFrame information
print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nFirst few rows:")
print(df.head())