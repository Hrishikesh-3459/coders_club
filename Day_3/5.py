# Write a program to display fibonacci series upto certain number n
n = int(input("Please enter a number: "))
a = 0
b = 1
print(a)
print(b)
while True:
    c = a + b
    if c > n:
        break
    print(c)
    a = b
    b = c