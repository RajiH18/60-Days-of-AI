name = input("Enter student name: ")

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")

    else:
        if marks >= 90:
            performance = "Excellent"

        elif marks >= 75:
            performance = "Very Good"

        elif marks >= 50:
            performance = "Good"

        else:
            performance = "Needs Improvement"

        print("\nStudent:", name)
        print("Marks:", marks)
        print("Performance:", performance)

except ValueError:
    print("Invalid marks. Please enter a number.")