import re

string = input().strip()
m = re.findall(r"([A-Za-z0-9])\1+", string)
if m:
    print(m[0])
else:
    print(-1)
