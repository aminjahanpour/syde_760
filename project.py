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

import numpy as np
from scipy.optimize import minimize


def eval(x):
    u1 = x[0]
    u2 = x[1]
    u3 = x[2]
    s1 = x[3]
    s2 = x[4]
    s3 = x[5]

    return -(2 * (u1 + u2 + u3) + (s1 + s2 + s3))


initial_solution = -2 + (2 + 2) * np.random.random()

ans = minimize(eval, initial_solution, method='nelder-mead', options={'maxiter': 1000, 'xtol': 1e-8, 'disp': True})
print(ans)
