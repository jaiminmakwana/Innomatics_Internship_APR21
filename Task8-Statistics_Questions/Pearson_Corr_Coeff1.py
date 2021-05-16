n = int(input())
x = list(map(float, input().strip().split()))
y = list(map(float, input().strip().split()))

mean_x = sum(x) / n
mean_y = sum(y) / n

std_x = (sum([(i - mean_x)**2 for i in x]) / n)**0.5
std_y = (sum([(i - mean_y)**2 for i in y]) / n)**0.5

covar = sum([(x[i] - mean_x) * (y[i] -mean_y) for i in range(n)])

corr_coeff = covar / (n * std_x * std_y)

print(round(corr_coeff, 3))