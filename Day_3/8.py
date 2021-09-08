n = int(input("Please enter a number: "))
i = 10
while n > 0:
    x = n % i
    print(x, end="")
    n -= x
    n //= i
print()
