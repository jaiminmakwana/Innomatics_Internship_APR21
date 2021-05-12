val = input().split()

arr = map(int, input().split())
lst = list(arr)

arr = map(int, input().split())
a = set(arr)

arr = map(int, input().split())
b = set(arr)

happiness = 0

if len(lst) <= 10**5 and len(a) <= 10**5 and len(b)<=10**5:
    for i in lst:
        for j in a:
            if i == j:
                # print("a", i)
                happiness += 1

        for k in b:
            if i == k:
                # print("b", i)
                happiness -= 1

    print(happiness)