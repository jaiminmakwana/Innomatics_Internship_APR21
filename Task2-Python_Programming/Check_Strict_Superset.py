avals = input().split()
avals = set(map(int, avals))
ans = []
if 0 < len(avals) < 501:
    tc = int(input())
    if 0 < tc < 21:
        for i in range(tc):
            bvals = input().split()
            bvals = set(map(int, bvals))
            if 0 < len(bvals) < 101:
                if len(avals) > len(bvals) and bvals.issubset(avals):
                    ans.append(True)

                else:
                    ans.append(False)

temp = 0
for i in ans:
    if not i:
        print("False")
        temp = 1

if temp == 0:
    print("True")