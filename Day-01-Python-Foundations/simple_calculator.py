# Day 1 - Simple Python Calculator

print("--- Simple Python Calculator ---")

str_num1 = input("Enter the first number: ")
str_num2 = input("Enter the second number: ")

num1 = float(str_num1)
num2 = float(str_num2)

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2

is_equal = num1 == num2

print("--- Calculation Results ---")

print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {diff_result}")
print(f"Multiplication: {num1} * {num2} = {prod_result}")
print(f"Division: {num1} / {num2} = {div_result}")
print(f"Numbers Equal: {is_equal}")