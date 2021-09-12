# Write a program to convert binary number to decimal manually 
def bin_to_dec(s):
    ans = 0
    for n,i in enumerate(s[::-1]):
        val = int(i) * (2 ** n)
        ans += val
    return ans


s = input("Please enter the binary number: ")
print(f"{s} as decimal number is : {bin_to_dec(s)}")