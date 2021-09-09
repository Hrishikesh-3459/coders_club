# Write a program to check whether a number is prime or not
n = int(input("Please enter a number: "))
for i in range(2, n//2):
    if n % i == 0:
        print("The number is not prime")
        break


# Special python feature where this is executed only if the above loop ends normally i,e without a break statement

else:
    print("The number is prime")
