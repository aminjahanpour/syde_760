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


import cma
import matplotlib.pyplot as plt
import numpy as np
from dfoalgos.simplex import NelderMeadSimplexSearch



"""
fixed settings
"""
N = 100000
cv = 1.0
budget = 1000
"""
fixed inflow realizations
"""
inflow = np.random.normal(6, 6 * cv, N)
inflow_1 = np.array([x if x >= 0 else 0 for x in inflow])

inflow = np.random.normal(9, 9 * cv, N)
inflow_2 = np.array([x if x >= 0 else 0 for x in inflow])

inflow = np.random.normal(7, 7 * cv, N)
inflow_3 = np.array([x if x >= 0 else 0 for x in inflow])

inflows = np.array([inflow_1, inflow_2, inflow_3]).T


#objective function
def cvar_obj(u, simu=False):

    f = []

    for I in inflows:
        S = [0, 0, 0, 0]

        S[0] = 2
        S[1] = S[0] + I[0] - u[0]  # S[1]
        S[2] = S[1] + I[1] - u[1]  # S[2]
        S[3] = S[2] + I[2] - u[2]  # S[3]

        if all([0 <= x <= 6 for x in S]):
            f.append(2 * (u[0] + u[1] + u[2]) + (S[1] + S[2] + S[3]))

    f.sort()

    min_f = min(f)
    max_f = max(f)

    var_a = 0

    frange = np.arange(min_f, max_f, 0.001)
    for f_idx , f_ in enumerate(frange):
        if (f_ - min_f) / (max_f - min_f) > alfa:
            var_a = f_
            # f_sub=f[:f_idx]
            break
    # cvar_a = np.mean([x for x in f if x <= var_a])


    f_sub=[x for x in f if x <= var_a]
    cvar_a=np.mean(f_sub)


    if simu:
        return var_a, cvar_a, f_sub

    else: #objective function for maximization
        return -cvar_a


def optimization():
    initial_solution = np.array([3, 3, 3])
    bnds = ((0, 6), (0, 6), (0, 6))

    """
    CMA optimization method
    """
    es = cma.CMAEvolutionStrategy(initial_solution, 0.5, {'bounds': [0, 6]})
    ans = es.optimize(cvar_obj, maxfun=budget, verb_disp=0)
    return [round(xx, 2) for xx in ans.best.x], round(ans.best.f, 2)

    """
    Simplex optimization method
    """
    # ans = NelderMeadSimplexSearch.minimize(cvar_obj, initial_solution, max_iterations=budget, bounds=bnds, disp=False)
    #
    # return [round(xx, 2) for xx in ans.x], round(ans.fun, 2)



def plot_hist(var_a, cvar_a, f):
    fig = plt.figure()
    fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title('axes title')
    ax.set_xlabel('Z')
    ax.set_ylabel('Frequency')
    # ax.text(3, 8, 'boxed italics text in data coords', style='italic',
    #         bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    ax.text(var_a, -12, r'$VaR_a$', fontsize=10)
    ax.text(cvar_a - 4, -12, r'$CVaR_a$', fontsize=10)
    plt.hist(f)
    plt.scatter([var_a, cvar_a], [0, 0], c='r')
    plt.xlabel("")
    plt.ylabel("")
    plt.show()





if __name__ == '__main__':

    fig = plt.figure()
    fig.suptitle('Cv=%2.2f' %cv, fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)

    means_res = []
    std_res = []

    for alfa in [0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2]:
        dv_opt, f_opt = optimization()

        var_a, cvar_a, f = cvar_obj(dv_opt, simu=True)

        x = np.std(f)
        y = np.mean(f)

        print("cv:%4.2f alfa:%6.3f VaR_a:%6.3f CVaR_a:%6.3f mean-benefit:%6.3f std-benefit:%6.3f" % (
            cv, alfa, var_a, cvar_a, y, x), 'optimum benefit function', -f_opt, 'optimum releases:', dv_opt)

        means_res.append(x)
        std_res.append(y)

        ax.text(x, y, alfa)

        plt.scatter(x=x, y=y)

    plt.xlabel("std")
    plt.ylabel("mean")

    plt.show()
