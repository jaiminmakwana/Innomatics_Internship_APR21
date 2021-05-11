import numpy as np

n = int(input())
lst = []
for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)
a = np.array(lst).reshape(n, n)
lst = []
for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)
b = np.array(lst).reshape(n, n)

print(np.dot(a, b))