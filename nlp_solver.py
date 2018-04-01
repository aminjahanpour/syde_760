import numpy as np
from scipy.optimize import minimize


def eval(x):
    x = x[0]
    return 66. * x ** 6 + 70. * x ** 5 - 320. * x ** 4 - 400. * x ** 3 + 1000.


initial_solution = -2 + (2 + 2) * np.random.random()

ans = minimize(eval, initial_solution, method='nelder-mead', options={'maxiter': 1000, 'xtol': 1e-8, 'disp': True})
print(ans)
