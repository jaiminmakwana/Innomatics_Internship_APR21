tc = int(input())

for i in range(tc):
    na = int(input())
    avals = input().split()
    avals = set(map(int, avals))

    nb = int(input())
    bvals = input().split()
    bvals = set(map(int, bvals))

    if len(avals) == na and len(bvals) == nb:
        print(avals.issubset(bvals))
