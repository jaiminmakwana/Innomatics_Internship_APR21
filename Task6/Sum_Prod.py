import numpy as np

n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)

array = np.array(lst).reshape(n, m)

print(np.prod(np.sum(array, axis=0)))