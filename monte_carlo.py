import math

import matplotlib.pyplot as plt
import numpy as np


def Q_fun(u):
    return (1.0 / u[2]) * u[0] * pow(u[1], (2. / 3.)) * pow(u[3], 0.5)


no_nodes = 4

mu = [10, 1.15, 0.012, 0.0009]

ro = np.ones(shape=[no_nodes, no_nodes])

ro[0] = [1, 0.6, 0.1, 0]
ro[1] = [0.6, 1, 0.15, 0]
ro[2] = [0.1, 0.15, 1, 0]
ro[3] = [0, 0, 0, 1]

cv = [0.1] * no_nodes

c = np.zeros(shape=[no_nodes, no_nodes], dtype=float)
for i in range(no_nodes):  # rows
    for j in range(no_nodes):  # columns
        c[i][j] = 1.0 * mu[i] * mu[j] * cv[i] * cv[j] * ro[i][j]

N = 1000000

u = np.random.multivariate_normal(mu, c.tolist(), N)

Q_ = list(map(Q_fun, u))
Q_ = [value for value in Q_ if not math.isnan(value)]
Q = np.array(Q_)

print(np.mean(Q))
print(np.var(Q))
print(np.std(Q))

print("Prob{Q >= 25} = ", len([x for x in Q_ if x >= 25.]) / N)
print("Prob{Q >= 31} = ", len([x for x in Q_ if x >= 31.]) / N)
print("Prob{Q >= 50} = ", len([x for x in Q_ if x >= 50.]) / N)

plt.hist(Q, bins=100, label="Cv=%f" % cv[0], fc=(0, 0, 1, 0.5))

plt.xlabel("Q")
plt.ylabel("Frequency")
plt.legend()
plt.show()
