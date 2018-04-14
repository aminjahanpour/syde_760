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
from scipy.optimize import linprog


def lp_solve(t, cv, s_init, inflow):


    # t = 1
    # cv = 0.5

    if t == 1:          # mean = 6
        if cv == 0.5:   # sd = 3
            inflow_set = [1.5, 6, 12]
            #    ut, sf1,    su1,    sf2,    su2,    sf3,    su3
            c = [-2, 0.1359, 0.1359, 0.6826, 0.6826, 0.1573, 0.1573]
        if cv == 1:     # sd = 6
            inflow_set = [6, 15, 18]
            c = [-2, 0.6827, 0.6827, 0.1359, 0.1359, 0.0214, 0.0214]


    elif t == 2:          # mean = 9
        if cv == 0.5:   # sd = 4.5
            inflow_set = [2.25, 9, 18]
            #    ut, sf1,    su1,    sf2,    su2,    sf3,    su3
            c = [-2, 0.1359, 0.1359, 0.6827, 0.6827, 0.1573, 0.1573]
        if cv == 1:     # sd = 9
            inflow_set = [9, 22.5, 31.5]
            c = [-2, 0.6827, 0.6827, 0.1359, 0.1359, 0.0228, 0.0228]


    elif t == 3:          # mean = 7
        if cv == 0.5:   # sd = 3.5
            inflow_set = [1.75, 7, 14]
            #    ut, sf1,    su1,    sf2,    su2,    sf3,    su3
            c = [-2, 0.1359, 0.1359, 0.6827, 0.6827, 0.1587, 0.1587]
        if cv == 1:     # sd = 7
            inflow_set = [7, 17.5, 24.5]
            c = [-2, 0.6827, 0.6827, 0.1359, 0.1359, 0.0228, 0.0228]


    """
    inequality const:
    
    Ut - St <= It  -->  1 * Ut <= It + St
    Ut >= 0        --> -1 * Ut <= 0
    """

    A_ub = [
        [1,  0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0]
    ]


    b_ub = [inflow + s_init,
            0
            ]


    """
    equality constraints:
    
    I_t+SF1-SU1=5  -->  SF1 - SU1 = 5 - I_t
    I_t+SF2-SU2=6  -->  SF2 - SU2 = 6 - I_t
    I_t+SF3-SU3=7  -->  SF3 - SU3 = 7 - I_t
    
    
    """
    A_eq = [
        [0, 1, -1, 0, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 1, -1]
        ]

    b_eq = [inflow_set[0] - inflow,
            inflow_set[1] - inflow,
            inflow_set[2] - inflow
            ]

    no_bounds = (-100, 100)



    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=len(c)*[no_bounds])
    # print(res)
    return(res['x'][0])

"""
let's assume for t=1:
S1 = 2
I1 = 5
"""
S_1 = 2
I_1 = 6

u_1 = lp_solve(t=1, cv=0.5, s_init=S_1, inflow=I_1)
print("t=1", S_1, I_1, u_1)

"""
t=2
"""
S_2 = S_1 + I_1 - u_1
I_2 = 9

u_2 = lp_solve(t=2, cv=0.5, s_init=S_2, inflow=I_2)
print("t=2", S_2, I_2, u_2)

"""
t=3
"""
S_3 = S_2 + I_2 - u_2
I_3 = 7

u_3 = lp_solve(t=3, cv=0.5, s_init=S_3, inflow=I_3)
print("t=3", S_3, I_3, u_3)


"""
f(x)=∑(t=1:3){2u_t+s_t}
"""

f = 2 * (u_1+u_2+u_3) + (S_1+S_2+S_3)
print(f)