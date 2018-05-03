"""
Given the objective function maximize: f(x)=∑(t=1:3){2u_t+s_t}
subject to usual conservation constraints for all time periods t=1, 2, and 3.

Means of inflows in three periods are 6, 9, and 7 units and

storage is bounded between 0 and 6.

Assume inflows as i.i.d as normal with coefficient of variations of 0.5 or 1.

Calculate a frontier of means and std. deviations for the two cases from optimization

    and compare it with

        results from Monte-Carlo simulation.

Discuss and infer especially regarding the method.

Your method is simulation-optimization and the minimum number of scenarios expected is 1000.

"""

import matplotlib.pyplot as plt
import numpy as np


def cvar_obj(u):
    cv = 0.5
    inflows = np.array(
        [np.random.normal(6, 6 * cv, 1000), np.random.normal(9, 9 * cv, 1000), np.random.normal(7, 7 * cv, 1000)]).T
    f = []
    for I in inflows:
        S = [2, 0, 0, 0]
        S = [S[0],
             S[0] + I[0] - u[0],  # S[1]
             S[1] + I[1] - u[1],  # S[2]
             S[2] + I[2] - u[2],  # S[3]
             ]

        f.append(2 * (u[0] + u[1] + u[2]) + (S[1] + S[2] + S[3]))
    f.sort()
    alfa = 0.1

    min_f = min(f)
    max_f = max(f)

    var_a = 0

    for i in np.arange(min_f, max_f, 0.001):
        if (i - min_f) / (max_f - min_f) > alfa:
            var_a = i
            break

    cvar_a = np.mean([x for x in f if x <= var_a])

    return var_a, cvar_a, f


var_a, cvar_a, f = cvar_obj([2, 2, 2])

print("var_a = %6.3f, cvar_a = %6.3f" % (var_a, cvar_a))

plt.hist(f)
plt.scatter([var_a, cvar_a], [0, 0], c='r')
plt.show()
