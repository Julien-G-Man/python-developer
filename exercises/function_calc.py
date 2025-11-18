import math
import logging

logger = logging.getLogger(__name__)

# Functions to perform operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        # infinity
        i = 0
        while True:
            print(i)
            i += 10
            
def find_square_root(n):
    square_root = pow(n, 0.5)
    return  f"The {n} is {square_root}."        

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = b / (2*a)
        return f"One real root: {root}"
    else:
        return "No real roots"
  
# General factorial function    
def find_factorial(n):
    n_factor = 1
    for i in range(1, n+1):
        i += 1
        n_factor *= i
        if i == n:
            return f"\n{n} factorial = {n_factor}"
    
# used only for permutation and combination        
def factorial(n):
    n_factor = 1
    for i in range(1, n+1):
        i += 1
        n_factor *= i
        if i == n:
            return n_factor
        
def permutation(n, r):            
    perm = factorial(n) / factorial(n-r) 
    return f"\n{n} Permutation {r} = {perm}"

def combination(n, r):
    comb = factorial(n) / (factorial(n-r) * factorial(r)) 
    return f"\n{n} Combination {r} = {comb}"  

def differentiate(x, n, a, b, c):
    f = a * pow(x, n) + (b * x) + c
    dydx = a * n * pow(x, n-1) + b
    return dydx

# Main function to run the calculator
def run_calculator():
    print("=====| CALCULATOR |=====")
    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Find Square Roots")
    print("6. Solve Quadratic Equation")
    print("7. Find Factorial")
    print("8. Perform Permuation")
    print("9. Perform Combination")
    print("10. Differentiation")
    
    choice = input("\nEnter choice (1/2/3/4/5/6/7/8/9/10): ")
    print("")

    try:
        # sqare roots
        if choice == '5':
            print("---- SQUARE ROOTS ----")
            n = input("Enter a number: ")
            print(find_square_root(n)) 
            
        # quadratic eqns
        elif choice == '6':  
            print("---- QUADRATIC EQUATIONS ----")
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            print(solve_quadratic(a, b, c))
            
        # factorials  
        elif choice == '7':
            print("---- FACTORIALS ----")
            n = int(input("Enter the number: "))
            print(find_factorial(n))
        
        # permutation
        elif choice == '8':
            print("---- PERMUTATION ----")
            print("We're finding nPr")
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            print(permutation(n, r))
          
        # combinaion  
        elif choice == '9':
            print("---- COMBINATION ----")
            print("We're finding nCr")
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            print(combination(n, r))  
        
        elif choice == '10':
            print("---- DIFFERENTIATION ----") 
            print("Let's perform some simple differentiation...")
            print("Given then equation ax^n + bx + c")
            a = int(input("Enter the value of a: "))
            x = int(input("Enter the value of x: "))
            n = int(input("Enter the value of n: "))
            b = int(input("Enter the value of b: "))
            c = int(input("Enter the value of c: "))
            
            print(f"\nf(x) = {a}x^{n} + {b}x + {c}")
            if n-1 == 1:
                print(f"dy/dx = {a*n}x + {b}")
            else:
                print(f"dy/dx = {a*n}x^{n-1} + {b}")
            print(f"\ndy/dx = {differentiate(x, n, a, b, c)}, at x = {x}")
                     
        else:
            if 1 <= int(choice) <= 10:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            else:
                print("Invalid input! Choose from the given options.") 
                
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")  

# Run the calculator
run_calculator()