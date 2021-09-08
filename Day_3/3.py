# Write a program to generate multiplication table of a number
n = int(input("Please enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
