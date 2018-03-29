var = 582.5

mean = 34.05

q = 31

ep = mean - q

ans = 0.5 + 0.5 * (1. - 0.01 * var / pow(ep, 2))
print(ep, ans)
