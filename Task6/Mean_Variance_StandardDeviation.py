import numpy as np

n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)

array = np.array(lst).reshape(n, m)

m = np.mean(array, axis=1)
v = np.var(array, axis=0)
sd = np.std(array).round(11)
print(m)
print(v)
print(sd)