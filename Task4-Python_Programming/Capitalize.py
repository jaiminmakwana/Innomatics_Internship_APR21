s = input()
lst = s.split()
ans = str()
for i in range(len(lst)):
    temp = True
    for j in range(len(lst[i])):
        if temp:
            ans += lst[i][0].upper()
            temp = False

        else:
            ans += lst[i][j]
    ans += ' '

print(ans)


### Program Continuous...


