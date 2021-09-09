# Write a program to calculate power of a number without using inbuilt pow() function
base = int(input("Please enter the base number: "))
power = int(input("Please enter the power number: "))
ans = 1
for i in range(power):
    ans *= base
print(f"{base} to the power {power} is {ans}")
