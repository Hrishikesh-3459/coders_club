# Write a program to find factorial of a given number
n = int(input("Please enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial is: {fact}")