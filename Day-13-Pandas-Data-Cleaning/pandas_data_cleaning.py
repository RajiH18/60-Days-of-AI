import pandas as pd

# Creating a dataset with missing values and duplicate data
data = {
    "Name": ["Raji", "Anu", "Ravi", "Raji"],
    "Marks": [85, None, 72, 85],
    "Age": [21, 20, None, 21]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove rows containing missing values
df_dropna = df.dropna()

print("\nAfter dropna():")
print(df_dropna)

# Fill missing Marks with the average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter fillna():")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter drop_duplicates():")
print(df)