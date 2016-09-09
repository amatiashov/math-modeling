import numpy


def dichotomy_solver(function, l_bound, r_bound, limit=1E-15):
    iteration_counter = 0
    if function(l_bound) == 0:
        return l_bound
    if function(r_bound) == 0:
        return r_bound
    # If the function crosses the X-axis on the interval [l_bound, r_bound],
    # then the signs of the values are different.
    if function(l_bound) * function(r_bound) > 0:
        return None

    while abs(l_bound - r_bound) > limit:
        midpoint = l_bound + (r_bound - l_bound) / 2
        if function(r_bound) * function(midpoint) < 0:
            l_bound = midpoint
        else:
            r_bound = midpoint
        iteration_counter += 1
    return midpoint, iteration_counter


def ctan(x):
    return 1 / numpy.tan(x)

lst = dichotomy_solver(ctan, 1, 2)

print('answer: ', lst[0])
print('iteration count: ', lst[1])