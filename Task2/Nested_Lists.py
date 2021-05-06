lst = []
for i in range(int(input())):
    l = []
    name = input()
    l.append(name)
    score = float(input())
    l.append(score)
    lst.append(l)

score = []
for i in range(len(lst)):
    score.append(lst[i][1])

m = min(score)

lst1 = lst.copy()

for i in range(len(lst)):
    if lst[i][1] == m:
        lst1.pop(score.index(m))
        score.remove(m)

try:
    m = min(score)

    ansind = []
    for i in range(len(score)):
        if score[i] == m:
            ansind.append(i)

    # ansind.reverse()
    # print(ansind)

    for i in ansind:
        print(lst1[i][0])

except:
    print()
