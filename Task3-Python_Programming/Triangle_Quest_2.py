#  print a palindromic triangle of size N

# 1 => (10 - 1)/9 = 1, 1 * 1 = 1
# 2 => (100 - 1)/9 = 11, 11 * 11 = 121
# 3 => (1000 - 1)/9 = 111, 111 * 111 = 12321

N = int(input())

for i in range(1,N+1):
    print(int((10**i-1)/9)**2)


