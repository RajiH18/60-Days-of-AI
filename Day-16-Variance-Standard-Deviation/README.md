# 📊 Day 16 — Variance & Standard Deviation

## 🎯 Topic

**Variance & Standard Deviation**

Today I continued **Week 3: Mathematics for AI** as part of my 60-Day AI Learning Journey.

## 📚 What I Learned

* What is Variance?
* What is Standard Deviation?
* How to calculate variance step by step
* How to calculate standard deviation
* Population vs Sample
* How standard deviation helps measure data spread
* How outliers and data distribution affect the spread

## 🧠 Understanding the Concept

**Variance** tells us how far the data values are spread from the mean.

**Standard Deviation** is the square root of variance and represents the spread in the original units of the data.

### Easy way to remember

* **Mean** → Center of the data
* **Variance** → Squared spread
* **Standard Deviation** → Spread in original units

## 🐍 Python Implementation

I used Python's `statistics` module:

```python
import statistics

data = [2, 4, 6, 8, 10]

variance = statistics.pvariance(data)
standard_deviation = statistics.pstdev(data)

print("Variance:", variance)
print("Standard Deviation:", round(standard_deviation, 2))
```

### Output

```text
Variance: 8
Standard Deviation: 2.83
```

## ⚠️ Population vs Sample

| Data                     | Python Functions          |
| ------------------------ | ------------------------- |
| Entire population        | `pvariance()`, `pstdev()` |
| Sample from a population | `variance()`, `stdev()`   |

## 🛠️ Mini Project

### Student Marks Analysis

I analyzed the following student marks:

```text
60, 65, 70, 75, 80, 85, 90
```

The results were:

```text
Mean: 75
Variance: 100
Standard Deviation: 10.0
```

This helped me understand how standard deviation describes how much the values vary around the mean.

## 🔍 Practice & Comparison

I also compared two datasets:

```text
Dataset A: 10, 20, 30, 40, 50
Dataset B: 28, 29, 30, 31, 32
```

Both datasets have the same mean:

```text
Mean = 30
```

But their standard deviations are different because the data is spread differently.

## 💡 Key Takeaway

> **Mean tells us the center.**
> **Variance tells us the squared spread.**
> **Standard deviation tells us how spread out the data is in the original units.**

Understanding these concepts will help me when I move deeper into **Statistics and Machine Learning**.

## 🚀 Progress

**Day 16 completed ✅**

**16 days completed | 44 days to go**

Still learning, practicing, and improving one concept at a time. 🌱💻
