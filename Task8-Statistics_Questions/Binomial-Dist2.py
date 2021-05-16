defect, batch = [float(x) for x in input().split()]
qual = 100 - defect


def fact(n):
    return 1 if n < 2 else n * fact(n-1)


def n_k(n, k):
    return fact(n) / (fact(k) * fact(n-k))


def odds(target, other):
    q = target / (target+other)
    d = other / (target+other)
    return q, d


def atleast_k(n, k, reverse=False):
    total_odds = 0

    while k <= n:
        combos = n_k(n, k)
        quality, defective = odds(qual, defect)
        total_odds += combos * quality**k * defective**(n-k)
        k += 1

    if not reverse:
        return total_odds
    else:
        return 1-total_odds


ans1 = atleast_k(batch, batch-2)
ans2 = atleast_k(batch, batch-1, reverse=True)

print('{:0.3f}'.format(ans1))
print('{:0.3f}'.format(ans2))