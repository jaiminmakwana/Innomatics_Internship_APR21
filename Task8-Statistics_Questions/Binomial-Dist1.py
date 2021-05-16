def fact(n):
    return 1 if n == 0 else n*fact(n-1)


def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))


def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)


l, r = list(map(float, input().split(' ')))
odds = l / r

lst = []

# range is 3 to 6 because here, we need atleast 3 boys and families have exactly 6 children
for i in range(3, 7):
    lst.append(b(i, 6, odds / (1 + odds)))

print(round(sum(lst), 3))

# print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))
