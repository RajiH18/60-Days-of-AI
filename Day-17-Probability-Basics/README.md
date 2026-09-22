# 🎲 Day 17 — Probability Basics

## 🎯 Topic

**Probability — Basic Concepts & Conditional Probability**

Today I continued **Week 3: Mathematics for AI** as part of my 60-Day AI Learning Journey.

## 📚 What I Learned

- What probability means
- Experiment
- Outcome
- Sample Space
- Event
- Basic probability
- Complement of an event
- Conditional probability
- Probability in AI and Machine Learning

## 🧠 Basic Probability

Probability tells us how likely an event is to happen.

Formula:

**P(A) = Favourable Outcomes / Total Outcomes**

For example, when rolling a dice, the probability of getting an even number is:

```text
Favourable outcomes = 3
Total outcomes = 6

P(Even) = 3 / 6
        = 0.5
        = 50%

Conditional Probability

Conditional probability tells us the probability of an event when we already know that another event has happened.

Formula:

P(A|B) = P(A ∩ B) / P(B)

I practiced this using a student example to understand how the given condition changes the group of outcomes we consider.

🐍 Python Practice

I created a simple Dice Probability Calculator using Python.

def probability(favourable, total):
    return favourable / total

total_outcomes = 6
even_outcomes = 3

result = probability(even_outcomes, total_outcomes)

print("Probability:", result)
print("Percentage:", result * 100, "%")
💡 Key Takeaway

Today I understood that probability is not just about "chance". It helps us understand uncertainty and is an important concept in AI and Machine Learning.

🚀 Progress

Day 17 completed ✅

17 days completed | 43 days to go

Still learning, practicing, and improving one concept at a time. 🌱💻