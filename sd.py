import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math


fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(-5, 5, 1.0))
ax.set_yticks(np.arange(0, 1., 0.1))


mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))

plt.grid()

plt.show()