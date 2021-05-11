import numpy as np

n = int(input())
lst = []
for i in range(n):
    l = list(map(float, input().split()))
    lst.append(l)

m = np.array(lst).reshape(n, n)
mdet = np.linalg.det(m).round(2)
print(mdet)