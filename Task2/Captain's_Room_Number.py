k = int(input())

if 1 < k < 1000:
    lst = input().split()
    lst = list(map(int, lst))

    uniset = set(lst)
    unilist = list(uniset)

    for i in unilist:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        # print("i", i, " ", count)
        if count == 1:
            print(i)
            break
