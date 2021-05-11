import numpy as np

lst = list(map(int, input().split()))
if len(lst) == 9:
    mat = np.reshape(lst, (3,3))
    print(mat)
