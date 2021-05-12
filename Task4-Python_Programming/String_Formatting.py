n = int(input())
l = len(bin(n)) - 2

for i in range(1, n+1):
    x = ""
    for j in "doXb":
        if x:
            x += " "
        x += "{:>" + str(l) + j + "}"
    print(x.format(i, i, i, i))
