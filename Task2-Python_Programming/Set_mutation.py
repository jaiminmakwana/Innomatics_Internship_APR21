
n = int(input())
vals = input().split()
vals = set(map(int, vals))

iter = int(input())

for i in range(iter):
    lis = input().split()
    tot = int(lis[1])
    # print("lis ", lis)

    l = input().split()
    l = list(map(int, l))

    # print(vals)
    # print("l ", l)
    if lis[0] == 'intersection_update':
        vals.intersection_update(l)

    if lis[0] == 'update':
        vals.update(l)

    if lis[0] == 'symmetric_difference_update':
        vals.symmetric_difference_update(l)

    if lis[0] == 'difference_update':
        vals.difference_update(l)

print(sum(vals))
