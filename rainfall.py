"""
You have 28 days of daily rainfall data, which are given as x(4, 7), meaning that they are arranged by days 1 to 28 in four
rows and seven columns. In any computer language of your choice, write a simple computer program that will calculate the
weekly average rainfall and the monthly average rainfall.
"""


import numpy as np

a = np.random.rand(4, 7)
weekly_avg = [np.mean(x) for x in a]
month_avg = a.mean()

print("weekly_avg", weekly_avg)
print("month_avg", month_avg)
