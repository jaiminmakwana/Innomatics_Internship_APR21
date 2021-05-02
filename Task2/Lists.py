N = int(input())

lst = []

for i in range(N):
    l = input().split()   # for example ['input', '1']
    lst.append(l)

ans = []
for i in range(N):
    if lst[i][0] == 'insert':
        ind = int(lst[i][1])
        ele = int(lst[i][2])
        ans.insert(ind, ele)

    if lst[i][0] == 'print':
        print(ans)

    if lst[i][0] == 'remove':
        val = int(lst[i][1])
        ans.remove(val)

    if lst[i][0] == 'append':
        ans.append(int(lst[i][1]))

    if lst[i][0] == 'sort':
        ans.sort()

    if lst[i][0] == 'pop':
        ans.pop()

    if lst[i][0] == 'reverse':
        ans.reverse()
