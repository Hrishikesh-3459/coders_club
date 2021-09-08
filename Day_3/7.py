# Write a program to find LCM of two numbers entered by the user
x, y = list(map(int, input("Please enter two numbers: ").split()))
big = max(x, y)
while True:
    if (big % x == 0) and (big % y == 0):
        lcm = big
        break
    big += 1
print(f"LCM is: {lcm}")
