from math import erf

mean, std = [float(x) for x in input().split()]
q1 = int(input())
q23 = int(input())

fun = lambda x: 0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))

print(round((1-fun(q1)) * 100, 2))
print(round((1-fun(q23)) * 100, 2))
print(round((fun(q23)) * 100, 2))