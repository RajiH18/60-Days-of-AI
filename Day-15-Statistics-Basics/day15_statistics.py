import statistics

marks = [65, 70, 75, 80, 80, 85, 90, 95]

mean = statistics.mean(marks)
median = statistics.median(marks)
mode = statistics.mode(marks)

print("Student Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)