import numpy

numpy.set_printoptions(legacy='1.13')

n, m = list(map(int, input().split()))
print(numpy.eye(n, m, k=0))
# print(numpy.eye(n, m))

