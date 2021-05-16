from math import erf

x = int(input())
n = int(input())
mean = int(input())
sigma = int(input())

mean_new = n * mean
sigma_new = n**0.5 * sigma

def fun(x, mean, sigma):
    Z = (x - mean) / sigma
    return 0.5*(1 + erf(Z/2**0.5))

ans = fun(x, mean_new, sigma_new)
print(round(ans, 4))