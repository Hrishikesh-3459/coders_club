# Write a program to calculate power of a number using inbuilt pow() function
from math import pow
base = int(input("Please enter the base number: "))
power = int(input("Please enter the power number: "))
print(f"{base} to the power {power} is {pow(base, power)}")
