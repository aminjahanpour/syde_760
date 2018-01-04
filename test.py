import numpy as np
import matplotlib.pyplot as plt



x = np.arange(0.,1.,0.01)
s = 1.

f1 = lambda x: x - 0.5 * x ** 2.
f2 = lambda x: (s-x) - (s-x) ** 2.
# print(f1(x))
plt.plot(x, f1(x))

plt.show()