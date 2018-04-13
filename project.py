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


def lp_solve(S1 = 2, I = 5):

    #    ut, sf1,  su1,  sf2, su2, sf3,  su3
    c = [-2, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25]


    """
    inequality const:
    
    Ut - St <= It  -->  1 * Ut <= It + St
    Ut >= 0        --> -1 * Ut <= 0
    """

    A_ub = [
        [1,  0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0]
    ]


    b_ub = [I+S1,
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

    b_eq = [5 - I,
            6 - I,
            7 - I
            ]

    no_bounds = (-100, 100)



    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=len(c)*[no_bounds], options={"disp": True})
    print(res)
    return(res['x'][0])

print (lp_solve(S1 = 2, I = 5))