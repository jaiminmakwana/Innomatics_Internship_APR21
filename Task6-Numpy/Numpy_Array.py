import numpy as np


def arrays(arr):
    # complete this function
    # use numpy.array
    arr = arr[::-1]
    arr = np.array(arr, float)
    return arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)