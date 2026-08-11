
def f(x):
    return x**2 + 2*x - 3 

def false_position(a, b, error_tol): 
    counter = 1
    try:
        if not f(a) * f(b) <= 0:
            raise ValueError(f"Root not between {f(a)} and {f(b)}")
        #while True:
        for i in range(20):
            x = (a * f(b) - b * f(a)) / (f(b) - f(a))
            display(counter, a, b, x)
            if x - b <= error_tol: # root = x
                return x 
            if f(x) * f(a) < 0:
                a, b = a, x
            else:
                a, b = x, b
            counter += 1
    except Exception as e:
        print(f"Error: {e}")

def display(counter, a, b, x):
    print(f"{counter}             {a}    {b}    {x}")
    

a, b = 0, 3
error_tol = 0.05

print("Iteration     a    b    x")  

root = false_position(a, b, 0.05)    
print(f"\nRoot: {root}")