# 📊 Day 15 — Statistics Basics

## 🎯 Topic

**Mean, Median & Mode**

Today I started **Week 3: Mathematics for AI** as part of my 60-Day AI Learning Journey.

## 📚 What I Learned

* What is Statistics?
* Mean — Average value
* Median — Middle value
* Mode — Most frequently occurring value
* Difference between Mean, Median and Mode
* How outliers can affect the Mean
* Calculating statistics using Python

## 🐍 Python Concepts

I practiced using Python's built-in `statistics` module.

```python
import statistics

marks = [65, 70, 75, 80, 80, 85, 90, 95]

mean = statistics.mean(marks)
median = statistics.median(marks)
mode = statistics.mode(marks)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
```

## 🛠️ Mini Project

### Analyze a Dataset

I used a student marks dataset to calculate:

* Mean
* Median
* Mode

This helped me understand how different statistical measures describe the same dataset.

## ⚠️ Important Concept — Outliers

I learned that an extreme value can have a large effect on the **Mean**.

For example:

```text
10, 20, 30, 40, 1000
```

Here:

* Mean = 220
* Median = 30

This helped me understand why the Median can sometimes be more useful when a dataset contains extreme values.

## 💡 Key Takeaway

Statistics is not just about calculating numbers. It helps us understand data before applying Machine Learning techniques.

## 🚀 Progress

**Day 15 completed ✅**

**15 days completed | 45 days to go**

Still learning, practicing, and improving one day at a time. 🌱💻
