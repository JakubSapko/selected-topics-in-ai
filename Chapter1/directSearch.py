from typing import Callable #* aesthetics purpose
import math

#TODO: Implement a direct search method

#! Cost function definition
def func(x: float) -> float:
    return x ** 4 + 2*x + 1

#* Direct search method implementation
#* The Direct search (also known as Pattern search) is actually a family of optimization methods
#* Those methods do not need a gradient, therefore can be used on non-continous or diffrentiable functions
#* Optimization attempts to find the best match (the solution that has the lowest error value) in a multidimensional analysis space of possibilities.
#* via Wikipedia: https://en.wikipedia.org/wiki/Pattern_search_(optimization)


#@param: x0: starting point
#@param: dx: delta x - value of change
#@param: func: cost function

def directSearch(x0: float, dx: float, func: Callable) :
    f0 = func(x0)
    x1 = x0 + dx
    f1 = func(x1)
    if (f1 <= f0):
        dx = 2*dx
        x2 = x1 + dx
        f2 = func(x2)
        while (f2 < f1):
            if (f2 >= f1):
                return (x0, x2)
            else:
                x0 = x1
                x1 = x2
                f0 = f1
                f1 = f2
            dx = 2*dx
            x2 = x1 + dx
            f2 = func(x2)
        if (f2 >= f1):
            return (x0, x2)
    else:
        dx = 2*dx
        x2 = x0 - dx
        f2 = func(x2)
        while (f0 > f2):
            if (f0 <= f2):
                return (x2, x1)
            else:
                x1 = x0
                x0 = x2
                f1 = f0
                f0 = f2
            dx = 2*dx
            x2 = x0 - dx
            f2 = func(x2)
        if (f0 <= f2):
            return (x2, x1)


if __name__ == "__main__":
    print(f'x1 = {directSearch(2, 0.001, func)[1]}, x2 = {directSearch(2, 0.001, func)[0]}')