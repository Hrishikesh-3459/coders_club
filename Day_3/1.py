# Write a prgram to calculate Sum of first N natural numbers 
n = int(input("Please enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print(f"Total = {total}")
