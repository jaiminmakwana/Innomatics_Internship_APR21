n = int(input())
lst = input().split()

sett = set(map(int, lst))

if len(sett) == n:
    for i in sett:
        if 0 > i > 20:
            break

    counter = 0
    lis1 = []
    cmd = int(input())
    for c in range(cmd):
        lis = input().split()  # for example ['input', '1']
        lis1.append(lis)
        counter += 1
        if counter > 19:
            break

    ans = []

    for i in range(n):
        if lis1[i][0] == 'pop':
            sett.pop()

        if lis1[i][0] == 'discard':
            sett.discard(int(lis1[i][1]))

        if lis1[i][0] == 'remove':
            sett.remove(int(lis1[i][1]))


summ = sum(sett)
print(summ)




