*

pow, log

cdef
double
min_f(double
x, void * params) nogil:
# Extract params
cdef
double * ps = < double * > params
# Compute interior penalty function
cdef
double
barrier = (-1) * ps[0] * log(x - 1)
# Compute original function value
cdef
double
f = pow(x, 2)

return f + barrier


def solve(initial_point, penalty):
    """
    Minimises Cython function min_f using Brent's method, and
    returns the result of the minimisation.

    Arguments:
    initial_point -- initial guess at the minimum
    penalty -- the penalty parameter (rho)
    """
    cdef
    int
    status
    # Initialise counter
    cdef
    int
    iter = 0
    cdef
    int
    max_iter = 100

    # Initial region of convergence
    # NOTE that the region of convergence encompasses
    # all x's greated than 1
    cdef
    double
    a = 1.0 + 1e-12
    cdef
    double
    b = 100.0

    # Initialise the minimisation problem
    cdef
    gsl_function
    F
    cdef
    double * params = [penalty]
    F.function = & min_f
    F.params = params

    # Initialise Brent's method
    cdef
    gsl_min_fminimizer_type * T
    cdef
    gsl_min_fminimizer * s
    T = gsl_min_fminimizer_brent
    s = gsl_min_fminimizer_alloc(T)
    gsl_min_fminimizer_set(s, & F, initial_point, a, b)

    status = GSL_CONTINUE

    # Minimise...
    while (status == GSL_CONTINUE and iter < max_iter):
        iter = iter + 1
        status = gsl_min_fminimizer_iterate(s)

        minimum = gsl_min_fminimizer_x_minimum(s)
        a = gsl_min_fminimizer_x_lower(s)
        b = gsl_min_fminimizer_x_upper(s)

        status = gsl_min_test_interval(a, b, 0.001, 0.0)

        if status == GSL_SUCCESS:
            break

    return minimum


from interior import solve

# Initial minimum
minimum = 3

# Penalty parameter
penalties = map(lambda x: x / 10, range(9, 0, -1))

for penalty in penalties:
    # Minimise the modified problem, and feed in the result as
    # the new starting point
    minimum = solve(minimum, penalty)

    print("penalty=%.1f, minimum=%f" % (penalty, minimum))
