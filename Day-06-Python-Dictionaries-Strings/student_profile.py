name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
city = input("Enter your city: ")

student = {
    "name": name,
    "age": age,
    "course": course,
    "city": city
}

print("\n--- Student Profile ---")
print("Name:", student["name"].title())
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])