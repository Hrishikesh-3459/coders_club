# Full pyramid star pattern
for i in range(6):
    for j in range(0, 6-i):
        print(" ", end = "")
    for k in range(0, i+1):
        print("* ", end = "")
    print()