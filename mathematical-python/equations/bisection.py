def f(x):
    return x**3 -x - 2 

def bisection_method(a, b, error_tol):
    try:
        if not f(a) * f(b) < 0:
            raise ValueError("f(a)and f(b) must have different signs")
        counter = 1
        while True:
            c = (a + b) / 2
            display(counter, a, b, c)
            if (b - c) <= error_tol:
                root = c 
                return root
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
            counter += 1
    except Exception as e:
        print(f"Error performing bisection: {e}")
        

def display(counter, a, b, c):
    print(f"{counter}             {a}    {b}    {c}")
      
a, b = 0, 3
error_tol = 0.05

print("Iteration     a    b    c")  

root = bisection_method(a, b, error_tol)     
print(f"\nRoot: {root}")