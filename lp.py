"""

Minimize: f = -1*x[0] + 4*x[1] + 3*x[2]

Subject to:

-3 * x[0] + 1 * x[1] + 0 * x[2] <= 6

1  * x[0] + 2 * x[1] + 0 * x[2] <= 4

0  * x[0] + 0 * x[1] + 1 * x[2] = 2.5

where:

-inf <= x[0] <= inf
x[1] >= -3
x[2] = 2.5

"""

from scipy.optimize import linprog

c = [-1, 4, 3]


# inequality const:
A_ub = [[-3, 1, 0],
        [1, 2, 0]]

b_ub = [6, 4]


# equality const:
A_eq = [[0, 0, 1]]

b_eq = [2.5]


x0_bounds = (None, None)
x1_bounds = (-3, None)
x2_bounds = (None, None)

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(x0_bounds, x1_bounds, x2_bounds), options={"disp": True})
print(res)
