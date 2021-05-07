n = int(input())
sp1 = len((bin(n).replace('0b', '')))
# print(sp1)
sp2 = sp1 + 1
# print(sp2)
leni = len(str(n))
# print(leni)
sp = sp1-leni
# print(sp)
for i in range(1, n+1):
    print(str(i).rjust(sp1, ' '), end='')
    print((oct(i).replace('0o', '')).rjust(sp2, ' '), end='')
    print((hex(i).replace('0x', '')).rjust(sp2, ' '), end='')
    print((bin(i).replace('0b', '')).rjust(sp2, ' '), end='')
    print()
