a = set()
b = set()
m = int(input())

lst = input().split()

newlis = list(map(int, lst))

# print(newlis)
temp = 0
for i in newlis:
    a.add(i)
    temp += 1
    if temp == m:
        break

n = int(input())

lst1 = input().split()

newlis1 = list(map(int, lst1))

print(newlis1)
temp = 0
for i in newlis1:
    b.add(i)
    temp += 1
    if temp == n:
        break

# print("a", a, "b", b)
a = sorted(a)
b = sorted(b)
# print("sorted a", a, "b", b)
ans = set()

for i in range(m):
    if a[i] == b[i]:
        pass
    else:
        for j in range(i, len(a)):
            ans.add(a[j])
        break

for i in range(n):
    if a[i] == b[i]:
        pass
    else:
        for j in range(i, len(b)):
            ans.add(b[j])
        break

ans = sorted(ans)

for i in ans:
    print(i)


