import numpy as np

n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    num = list(map(int, input().split()))
    lst.append(num)
matrix1 = np.array(lst).reshape(n, m)

lst = []
for i in range(n):
    num = list(map(int, input().split()))
    lst.append(num)
matrix2 = np.array(lst).reshape(n, m)

print(np.add(matrix1, matrix2))
print(np.subtract(matrix1, matrix2))
print(np.multiply(matrix1, matrix2))
print(np.floor_sdivide(matrix1, matrix2))
print(np.mod(matrix1, matrix2))
print(np.power(matrix1, matrix2))