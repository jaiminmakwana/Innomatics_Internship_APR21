k = int(input())

if 1 < k < 1000:
    lst = input().split()
    lst = list(map(int, lst))

    uniset = set(lst)
    unilist = list(uniset)

    for i in unilist:
        temp = 0
        count = 0
        for j in lst:
            if i == j:
                count += 1
                if count > 1:
                    temp = 1
                    break
        if temp == 0:
            print(i)
            break
