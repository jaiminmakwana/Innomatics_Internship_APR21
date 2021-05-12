import math
n, m = input().split()
n = int(n)
m = int(m)

midrow = math.ceil(n/2)
# middle = math.ceil(m/2)
temp = 1
str = '.|.'
str1 = str
for i in range(0, midrow):
    if i == midrow-1:
        print('WELCOME'.center(m, '-'))

    else:
        print(str1.center(m, '-'))
        # print(len(str1))
        str1 = str1 + 2 * str
        # print(str1)
        temp += 2
        # print(temp)

temp -= 2

for i in range(midrow, n):
    str2 = str * temp
    print(str2.center(m, '-'))
    temp -= 2

