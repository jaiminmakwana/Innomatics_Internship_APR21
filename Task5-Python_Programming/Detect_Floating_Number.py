import re

lst = []
for i in range(int(input())):
    lst.append(input())
for i in lst:
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', i)))