from math import erf

tickets = int(input())
n = int(input())
mean = float(input())
sd = float(input())

nmean = n * mean
nsd = n**0.5 * sd


def fun(t, mean, sigma):
    Z = (t - mean)/sigma
    return 0.5*(1 + erf(Z/2**0.5))

ans = fun(tickets, nmean, nsd)
print(round(ans, 4))