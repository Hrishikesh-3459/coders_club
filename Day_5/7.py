# Hollow full pyramid star
for i in range(6):
    for j in range(0, 6-i):
        print(" ", end = "")
    for k in range(0, i+1):
        if i in range(1, 5) and k in range(1, i):
            print("  ", end = "")
        else:
            print("* ", end = "")
    print()