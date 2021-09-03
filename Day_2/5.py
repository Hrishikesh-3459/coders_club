# Write a program to check whether a year entered by user is leap year or not
y = int(input("Please enter the year: "))
if (y % 400 == 0):
    print("Leap Year")

elif (y % 100 == 0):
    print("Not Leap Year")

elif (y % 4 == 0):
    print("Leap Year")

else:
    print("Not Leap Year")
