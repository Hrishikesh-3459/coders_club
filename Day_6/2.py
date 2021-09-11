# Write a program to check if an integer can be expressed as the sum of two prime numbers, if yes then print all possible combinations with the use of functions
def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Please enter the number: "))
primes = find_primes(n)
set_primes = set(primes)
for p in primes:
    diff = abs(n - p)
    if diff in set_primes:
        print(f"{n} = {diff} + {p}")
        set_primes.remove(p)
