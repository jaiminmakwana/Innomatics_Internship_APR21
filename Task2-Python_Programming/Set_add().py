N = int(input())
sett = set()
if 1000 > N > 0:
    for i in range(N):
        stamp = input()
        sett.add(stamp)

print(len(sett))
