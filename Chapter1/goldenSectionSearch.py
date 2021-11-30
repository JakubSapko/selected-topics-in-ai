from typing import Callable #* aesthetics purpose
import math

#TODO: Implement a golden section search method


#! Cost function definition
def func(x: float) -> float:
    return math.e ** (-x) + x ** 2

#* Golden-section search method implementation
#* The Golden-section search method is analogical to Fibonacii search method
#* Golden-section search is a limit of Fibonacci search
#* It is linearly convergent


#@param a: left constrain of given interval
#@param b: right constrain of given interval
#@param: eps: accuracy (the lower it is the more accurate the final result)
#@param: func: cost function (function that gets maximized or minimized

def goldenSearch(a: float, b: float, eps: float, func: Callable[[float], float]) -> float:

    ratio = (1+ math.sqrt(5)) / 2
    x1 = b + (a-b)/ratio
    x2 = a + (b-a)/ratio
    f1 = func(x1)
    f2 = func(x2)

    while (abs((b-a)) >= eps):
        if (f1 < f2):
            b = x2
            x2 = x1
            f2 = f1
            x1 = b + (a-b)/ratio
            f1 = func(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b-a)/ratio
            f2 = func(x2)
    return abs((a-b))/2



