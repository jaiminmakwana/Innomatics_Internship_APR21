from math import ceil

m = int(input())
n = m * 2 - 1
mid = ceil(n/2)
print(mid)
l = n + n - 1
upp = 96 + mid
upp1 = upp
temp = 0
str = 'z'
for i in range(1, mid+1):
    # print(upp)
    if upp+1 > upp1:
        print(chr(upp).center(l, '-'))
    else:
        print((chr(upp+1) + '-' + chr(upp) + '-' + chr(upp+1)).center(l, '-'))
    upp -= 1

low = 98
for i in range(mid, n):
    print(chr(low).center(l, '-'))
    low += 1

### Program Continuous...
