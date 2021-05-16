
samples = int(input())
mean = float(input())
sd = float(input())
interval = float(input())
z = float(input())

sd_sample = sd / (samples**0.5)
appz = sd_sample * z

print(round(mean - appz, 2))
print(round(mean + appz, 2))