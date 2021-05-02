n = int(input())
integer_list = map(int, input().split())
lst = []
for i in integer_list:
    lst.append(i)

t = tuple(lst)

print(hash(t))