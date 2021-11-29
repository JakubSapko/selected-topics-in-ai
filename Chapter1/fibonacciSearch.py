from typing import Callable #* aesthetics purpose

#TODO: Implement a fibonacci search method 

#! Cost function definition
def func(x: float) -> float:
    return x ** 4 + 2*x + 1

#* Fibonacci Search method implementation
#* The Fibonacci search method is usually used either for minimizing or maximizing a function on a given interval
#* This method is typically used in the unconstrained optimaztion problems


#@param: a: left constrain of given interval
#@param: b: right constaring of given interval
#@param: eps: accuracy (the lower it is the more accurate the final result)
#@param: func: cost function (the function you want to maximize/minimize)

def fibonacciSearch(a: float, b: float, eps: float, func: Callable[[float], float]) -> float:

    c = (b - a)/eps
    n = 1
    Fib = [0, 1, 1]

    while (Fib[n] < c):
        n += 1
        Fib.append(Fib[n-2] + Fib[n-1])

    k = 1
    x1 = a + (Fib[n-2]/Fib[n]) * (b - a)
    x2 = a + (Fib[n-1]/Fib[n]) * (b - a)
    f1 = func(x1)
    f2 = func(x2)

    while (k < n-2):
        if (f1 < f2):
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (Fib[n-k-2]/Fib[n-k]) * (b - a)
            f1 = func(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a+ (Fib[n-k-1]/Fib[n-k]) * (b - a)
            f2 = func(x2)
        k += 1

    if f1 < f2:
        b = x2
        x2 = x1
        f2 = f1
    else:
        a = x1

    x1 = x2 - 0.1*(b-a)
    f1 = func(x1)
    w = f1 - f2

    if w < 0:
        return 0.5*(a+x1)
    elif w == 0:
        return 0.5*(x1+x2)
    else:
        return 0.5*(x1+b)

