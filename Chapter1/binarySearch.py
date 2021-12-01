from typing import Callable #* aesthetics purpose
import math

#TODO: Implement a binary search method


#! Cost function definition
def derFunc(x: float) -> float:
    return x**2-x-1

#* Binary search (also known as half-interval search) implementation
#* Binary search is a searching algorithm which compares the target value to 
#* the middle point and if those are not equal it eliminates the midPoint
#* via Wikipedia: https://en.wikipedia.org/wiki/Binary_search_algorithm


#@param: a: left constarin of given interval
#@param: b: right constrain of given interval
#@param: func: cost function
#@param: N: number of iterations (substitute of epsilon as I didn't know how to make it any other approach than iterating)

def binarySearch(a: float, b: float, func: Callable[[float], float], N: int) -> float or None:
    fa = func(a)
    fb = func(b)
    if (fa * fb >= 0):
        print("Solution is not guaranteed")
        return None
    else:
        a_n = a
        b_n = b
        for n in range(1, N+1):
            midPoint = (a_n + b_n)/2
            fMP = func(midPoint)
            if ((func(a_n)*fMP) < 0):
                a_n = a_n
                b_n = midPoint
            elif ((func(b_n)*fMP)<0):
                a_n = midPoint
                b_n = b_n
            elif (fMP == 0):
                print("Found exact solution")
                return midPoint
            else: 
                print("Method failed")
                return None
    return (a_n + b_n)/2

if __name__ == "__main__":
    a = 1
    b = 2
    N = 1000
    print(f'Approximated minimum of function {derFunc.__name__} using Binary Search on a interval of [{a};{b}]: {binarySearch(a, b, derFunc, N)}')