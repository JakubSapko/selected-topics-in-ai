from typing import Callable #* aesthetics purpose
import math

#TODO: Implement a parabolic interpolation

#! NOTES:
'''
fi = f(xi)
phi(x) = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))*f1
       * ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))*f0
       * ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))*f2
phi'(x) = 0
x_dash = 0.5 * ((x2^2-x0^2)*f1 + (x1^2-x2^2)*f0 + (x0^2-x1^2)*f2)/((x2-x0)*f1+(X1-x2)*f0+(x0-x1)*f2)
'''

#! Cost function definition
def func(x):
    return x ** 4 + 2*x + 1

#* Parabolic interpolation is a technique for finding the extremum of a continous unimodal function
#* It is achieved by fitting parabolas to a function of one variable at three unique points
#* At each iteration the so called "oldest" point is replaced by a extremum of fitted parabola


#@param x0, x1, x2: unique points through which we will interpolate
#@param eps1, eps2: accuracies
#@param func: cost function
def parabolicInterpolation(x0, x1, x2, eps1, eps2, func):
    f0 = func(x0)
    f1 = func(x1)
    f2 = func(x2)
    x_dash = 0.5 * ((x2**2-x0**2)*f1 + (x1**2-x2**2)*f0 + (x0**2-x1**2)*f2)/((x2-x0)*f1+(x1-x2)*f0+(x0-x1)*f2)
    while ((abs(x0 - x_dash) > eps1)):
        if (abs((x2-x0)*f1 + (x1-x2)*f0 + (x0-x1)*f2) > eps2):
            break
        f_dash = func(x_dash)
        if (f0 < f_dash):
            if( x0<x_dash):
                x2 = x_dash
                f2 = f_dash
            else:
                x1 = x_dash
                f1 = f_dash
        elif (f0 == f_dash):
            if(x0<x_dash):
                f1 = f0
                f2 = f_dash
                f0 = func(x0)
            else:
                x1 = x_dash
                x2 = x0
                x0 = 0.5*(x1+x2)
                f1 = f_dash
                f2 = f0
                f0 = func(x0)
        elif (f0 > fd):
            if (x0 > x_dash):
                x2 = x0
                x0 = x_dash
                f2 = f0
                f0 = f_dash
            else:
                x1 = x0
                x0 = x_dash
                f1 = f0
                f0 = f_dash
    return (x0, f0)

if __name__ == "__main__":
    print(f'x0 = {parabolicInterpolation(1, 3, 4, 0.001, 0.01, func)[0]}, f0 = {parabolicInterpolation(1, 3, 4, 0.001, 0.01, func)[1]}')