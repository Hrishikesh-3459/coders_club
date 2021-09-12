# Write a program to convert decimal to binary number manually
def dec_to_bin(n):
    s = ""
    while n != 0:
        rem = int(n % 2)
        n //= 2
        s += str(rem)
    return s

n = int(input("Please enter a number: "))
print(f"{n} as binary number is : {dec_to_bin(n)}")
