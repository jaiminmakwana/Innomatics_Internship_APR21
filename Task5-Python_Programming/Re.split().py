import re
regex_pattern = r"[,.]+"  # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))
print(re.split(regex_pattern, input()))

# string = input().strip()
#
# s = string.split(',')
# l = len(s)
# s1 = s[l-1].split('.')
# for i in range(len(s)-1):
#     print(s[i])
#
# print(s1[0])
# print(s1[1])