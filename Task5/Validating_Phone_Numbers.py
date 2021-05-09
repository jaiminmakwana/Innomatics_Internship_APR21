import re

for i in range(int(input())):
    m = re.match(r'[789]\d{9}$', input())
    if m:
        print('YES')
    else:
        print('NO')