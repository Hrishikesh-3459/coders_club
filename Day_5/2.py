# Hollow rectangular star
for i in range(3):
    for j in range(5):
        if i == 1 and j in [1, 2, 3]:
            print("  ", end = "")
        else:
            print("* ", end = "")
    print()