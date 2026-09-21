import statistics

marks = [60, 65, 70, 75, 80, 85, 90]

mean = statistics.mean(marks)
variance = statistics.pvariance(marks)
std_dev = statistics.pstdev(marks)

print("Student Marks:", marks)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", round(std_dev, 2))