
def dichotomy_solver(function, l_bound, r_bound, epsilon=1E-15):
    iteration_counter = 0
    if function(l_bound) == 0:
        return l_bound
    if function(r_bound) == 0:
        return r_bound
    # If the function crosses the X-axis on the interval [l_bound, r_bound],
    # then the signs of the values are different.
    if function(l_bound) * function(r_bound) > 0:
        return None

    while abs(l_bound - r_bound) > epsilon:
        midpoint = l_bound + (r_bound - l_bound) / 2
        if function(r_bound) * function(midpoint) < 0:
            l_bound = midpoint
        else:
            r_bound = midpoint
        iteration_counter += 1
    return midpoint, iteration_counter


def chord_method(f, a, b, epsilon=1E-15):
    iteration_counter = 0
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    # If the function crosses the X-axis on the interval [l_bound, r_bound],
    # then the signs of the values are different.
    if f(a) * f(b) > 0:
        return None

    while abs(b - a) > epsilon:
        a = b - (b - a) * f(b) / (f(b) - f(a))
        b = a + (a - b) * f(a) / (f(a) - f(b))
        iteration_counter += 1

    return b, iteration_counter