# Day 13 - Pandas Data Cleaning

## What I Learned

Today I learned how to clean data using Pandas.

### Topics Covered

- Handling missing values
- `dropna()` - remove rows with missing values
- `fillna()` - fill missing values
- Finding the average using `mean()`
- `drop_duplicates()` - remove duplicate rows
- Basic data cleaning techniques

## Practice Dataset

I worked with a dataset containing:

- Name
- Marks
- Age

The dataset had missing values and duplicate rows.

## Operations Performed

### 1. Removing Missing Values

```python
df.dropna()
```

### 2. Filling Missing Values

```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

### 3. Removing Duplicate Rows

```python
df.drop_duplicates()
```

## Key Takeaway

Data cleaning is an important step before data analysis and Machine Learning. Pandas provides simple functions to handle missing and duplicate data efficiently.

## Technologies Used

- Python
- Pandas

**Day 13/60 - 60 Days of AI Learning Journey 🚀**