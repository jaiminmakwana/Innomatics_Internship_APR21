x, y = [], []

for j in range(5):
    i = input().split()
    x.append(int(i[0]))
    y.append(int(i[1]))
n = len(x)
x_sum = sum(x)
x_sum_sqr = x_sum**2
x_sqr_sum = sum([x_i**2 for x_i in x])
y_sum = sum(y)
sum_prod_xy = 0
for x_i, y_i in zip(x, y):
    sum_prod_xy += (x_i * y_i)
ans1 = (n * sum_prod_xy - x_sum * y_sum) / (n * x_sqr_sum - x_sum_sqr)
y_mean = y_sum/n
x_mean = x_sum/n
ans2 = y_mean - ans1 * x_mean

# prediction
x_test = 80
y_test = ans2 + ans1 * x_test
print("{:.3f}".format(y_test))