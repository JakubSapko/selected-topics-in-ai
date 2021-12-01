
#* This code is to test and present the following problem's outcome:
#* Minimize f(x) = e^(-x) + x^2 on the interval of [a, b] = [0, 1]

from goldenSectionSearch import goldenSearch, func

if __name__ == "__main__":
    a = 0
    b = 1
    eps = 1
    print(f'Approximated minimum of function: {func.__name__}, between points {a} and {b} with accuracy of epsilon = {eps} using Golden-section search was found at: {goldenSearch(a, b, eps, func)}')