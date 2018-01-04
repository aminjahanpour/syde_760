import numpy as np
import matplotlib.pyplot as plt



x = np.arange(0.,1.,0.01)
s = 1.

f1 = lambda x: x - 0.5 * x ** 2.
f2 = lambda x: (s-x) - (s-x) ** 2.
# print(f1(x))
plt.plot(x, f1(x),label='f1')
plt.plot(x, f2(x),label='f2')
plt.plot(x, f1(x) + f2(x),label='f1+f2')

plt.scatter(x=[2./3.], y=[2./3.], label='optimum')

plt.legend()

plt.show()