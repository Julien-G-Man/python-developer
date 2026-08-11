import numpy as np

def f(x):
    return x**2 + 2*x - 3 


def lagrange(x):
    return

def newton_raphson(x0, error_tol):
    counter = 1
    try:
        while True:
            dydx = np.gradient(f(x0), x0)
            x1 = x0 - f(x0)/(dydx)
            if x1 - x0 <= error_tol:
                return x1
            x0 = x1
            counter += 1
    except Exception as e:
        print("error: ", e)