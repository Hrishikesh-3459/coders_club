# Write a program to display prime numbers between two intervals
def isPrime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

low = int(input("Please enter start: "))
high = int(input("Please enter end: "))
ans = []
for i in range(low, high):
    if isPrime(i):
        if i not in [0, 1]:
            ans.append(str(i))
print(f"Prime numbers between {low} and {high} are: {' '.join(ans)}")
