import numpy as np

def f(x):
    return x**3 - x - 2 

def secant(a, b, error_tol):
    counter = 1
    try:
        while True:
            x = b - f(b) * ( (b - a) / (f(b) - f(a)) )
            display(counter, a, b, x, f(x))
            if x - b <= error_tol:
                return x
            a = b, b = x
            counter += 1
    except Exception as e:
        print("Error: ", e)
        
        
a, b = 1, 2
error_tol = 0.05

def display(counter, a, b, x, fx):
    print(f"{counter}             {a}    {b}    {x}  {fx}")
      

print("Iteration     a    b    x                    fx")  

root = secant(a, b, error_tol)     
print(f"\nRoot: {root}")

