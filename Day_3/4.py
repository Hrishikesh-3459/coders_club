# Write a program to display fibonacci series upto nth term
n = int(input("Please enter a number: "))
i = 2
a = 0
b = 1
print(a)
print(b)
while i < n:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1