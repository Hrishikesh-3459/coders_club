# Write a program to display all factors of a number entered by User
n = int(input("Please entere a number: "))
factors = []
for i in range(1, (n//2) + 1):
    if n % i == 0:
        factors.append(str(i))
print(f"The factors of {n} are: {' '.join(factors)}")
