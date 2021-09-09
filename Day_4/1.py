# Write a program to display the sum of all digits of a given number N by user
n = input("Please enter a number: ")
total = 0
for i in n:
    total += int(i)
print(f"The sum is: {total}")
