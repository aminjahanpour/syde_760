import numpy as np
a = np.random.rand(4,7)
weekly_avg = [np.mean(x) for x in a]
month_avg = a.mean()
