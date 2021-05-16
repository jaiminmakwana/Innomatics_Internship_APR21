from math import erf

mean, std = [float(x) for x in input().split()]

def ndist(x):
    return 0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(ndist(19.5)))

# Between 20 and 22
print('{:.3f}'.format(ndist(22) - ndist(20)))
