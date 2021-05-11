import numpy as np

r, c = input().split()
r = int(r)
c = int(c)
lst = []
for i in range(r):
    num = list(map(int, input().split()))
    lst.append(num)

matrix = np.array(lst).reshape(r, c)
tmatrix = matrix.transpose()
print(tmatrix)
fmatrix = matrix.flatten()
print(fmatrix)
