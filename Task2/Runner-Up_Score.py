
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

lst = list(arr)
maxi = max(lst)

lst1 = lst.copy()
for i in range(len(lst)):
    if lst[i] == maxi:
        lst1.remove(maxi)

print(max(lst1))