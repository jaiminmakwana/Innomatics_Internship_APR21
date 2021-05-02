val = input().split()
n = int(val[0])
m = int(val[1])
a = set()
b = set()

arr = map(int, input().split())
lst = list(arr)

arr = map(int, input().split())
y = list(arr)
for i in range(m):
    a.add(y[i])

arr = map(int, input().split())
y = list(arr)
for i in range(m):
    b.add(y[i])

# print(lst, a, b)

happiness = 0

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

