
#* This code is to test and show the following problem:
#* Minimize f(x) = x^4 + 2x + 1 in the interval of [a, b] = [-1, 0]

from fibonacciSearch import fibonacciSearch, func

if __name__ == "__main__":
    a = 0
    b = 1
    eps = 0.0001
    print(f'Approximated minimum of function: {func.__name__}, between points {a} and {b} with accuracy of epsilon = {eps} using Fibonacci Search was found at: {fibonacciSearch(a, b, eps, func)}')