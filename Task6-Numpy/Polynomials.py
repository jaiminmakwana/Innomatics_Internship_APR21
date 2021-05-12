import numpy as np

lst = list(map(float, input().split()))
x = int(input())
pval = np.polyval(lst, x)
print(pval)