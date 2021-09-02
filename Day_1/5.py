# Write a program to find size of int, float, double and char on your computer
from sys import getsizeof
a = int(5)
b = float(5.0)
c = "x"
print(f"The size of int is: {getsizeof(a)}")
print(f"The size of float is: {getsizeof(b)}")
print(f"The size of char is: {getsizeof(c)}")