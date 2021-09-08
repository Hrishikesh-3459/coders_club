# Write a program to find GCD or HCF of two numbers entered by the user
x, y = list(map(int, input("Please enter two numbers: ").split()))
small = min(x, y)
for i in range(1, small + 1):
    if (x % i == 0) and (y % i == 0):
        gcd = i
print(f"GCD is {gcd}")