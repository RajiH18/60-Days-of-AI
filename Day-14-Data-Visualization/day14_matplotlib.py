import matplotlib.pyplot as plt

# -------------------------------
# 1. Bar Chart
# -------------------------------

students = ["Ravi", "Anu", "Priya", "Kiran"]
marks = [78, 92, 65, 88]

plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()


# -------------------------------
# 2. Line Chart
# -------------------------------

days = [1, 2, 3, 4, 5]
progress = [60, 65, 70, 78, 85]

plt.plot(days, progress, marker="o")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.title("Student Progress")
plt.show()


# -------------------------------
# 3. Scatter Plot
# -------------------------------

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 60, 68, 78, 88]

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()


# -------------------------------
# 4. Histogram
# -------------------------------

marks = [45, 50, 55, 60, 62, 65, 68, 70,
         72, 75, 80, 85, 90, 95]

plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()


# -------------------------------
# 5. Pie Chart
# -------------------------------

subjects = ["Python", "Java", "SQL", "ML"]
hours = [10, 8, 5, 7]

plt.pie(hours, labels=subjects, autopct="%1.1f%%")
plt.title("Study Time Distribution")
plt.show()