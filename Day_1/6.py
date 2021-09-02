# Write a program to swap two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Numbers before swapping a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"Numbers after swapping a = {a}, b = {b}")