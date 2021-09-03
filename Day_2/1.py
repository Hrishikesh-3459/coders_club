# Write a program to check whether number is even or odd
n = int(input("Please enter a number: "))
if n & 1 == 0:
    print("Number is even")
else:
    print("Number is odd")