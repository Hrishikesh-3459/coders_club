# Write a program to check whether a number N entered by user is palindrome or not
n = input("Please enter a number: ")
if n == n[::-1]:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")