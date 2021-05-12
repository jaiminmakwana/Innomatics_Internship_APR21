import cmath
from math import sqrt
num = complex(input())

val1 = sqrt(num.imag**2 + num.real**2)

val2 = cmath.phase(num)

print(val1)
print(val2)