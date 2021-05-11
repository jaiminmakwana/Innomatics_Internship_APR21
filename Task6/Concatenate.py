import numpy as np

lst = list(map(int, input().split()))
n, m, p = lst[0], lst[1], lst[2]
array_1 = []
array_2 = []
for i in range(n):
    num = list(map(int, input().split()))
    array_1.append(num)

for i in range(m):
    num = list(map(int, input().split()))
    array_2.append(num)

print(np.concatenate((array_1, array_2), axis=0))