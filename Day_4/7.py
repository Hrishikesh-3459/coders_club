# Write a program to check whether a number entered by the user is Armstrong number or not
n = int(input("Please enter a number: "))
total = 0
l = len(str(n))
for i in str(n):
    total += (int(i) ** l)
if total == n:
    print("The given number is an Armstrong number")
else:
    print("The given number is NOT and armstrong number")
    