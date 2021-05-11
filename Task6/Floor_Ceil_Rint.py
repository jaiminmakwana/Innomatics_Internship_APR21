import numpy as np

np.set_printoptions(legacy='1.13')
num = list(map(float, input().split()))

print(np.floor(num))
print(np.ceil(num))
print(np.rint(num))