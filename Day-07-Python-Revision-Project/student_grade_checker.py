name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
marks = int(input("Enter your marks: "))

student = {
    "name": name,
    "age": age,
    "course": course,
    "marks": marks
}


def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


grade = get_grade(student["marks"])

print("\n===== STUDENT PROFILE =====")
print("Name:", student["name"].title())
print("Age:", student["age"])
print("Course:", student["course"].title())
print("Marks:", student["marks"])
print("Grade:", grade)
print("===========================")