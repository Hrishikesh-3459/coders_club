# Pascal's triangle
arr = [[0, 0, 1, 0, 0]]
for i in range(4):
    tmp = arr[-1]
    n = [0]
    for j in range(1, len(tmp)):
        val = tmp[j-1] + tmp[j]
        n.append(val)
    n.append(0)
    arr.append(n)

counter = 4
for i in arr:
    print(" " * counter, end = "")
    counter -= 1
    for j in i:
        if j == 0:
            print(" ", end = "")
        else:
            print(str(j) + " ", end = "")
    print()

