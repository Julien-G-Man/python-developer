import math
import logging

logger = logging.getLogger(__name__)

print("select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quadratic equations")
print("6. Factorials")

opt = input("Choose the operation you wantn to make [1/2/3/4/5/6]: ")

if opt != '5' and opt != '6':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if opt == '1':
        print(f"The addition is: {num1 + num2}")
    elif opt == '2':
        print(f"The subtraction is: {num1 - num2}")    
    elif opt == '3':
        print(f"The multiplication is: {num1 * num2}")
    elif opt == '4':
        try:
            print(f"The division is: {num1 / num2}")  
        except Exception:
            num2 == 0
            logger.error("Error! The denominator cannot be zero.")
            
if opt == '5': 
    print("\n---- QUADRATIC EQUATIONS ---- \n")
    print("Quadratic equation: ax^2 + bx + c")   
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    
    if (a == 0 and b == 0) or a == 0:
        logger.error("Invalid Input. The equation is not quadratic!")
    elif a == 1 or b == 1:
        print(f"The quadratic equation is: x^2 + x + {c} = 0") 
    else:     
        print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0") 
    
    disc = (b**2) - 4*a*c
    if disc == 0:
        x = -b/(2*a)
        print(f"The roots are equal: {x}")
    elif disc > 0:
        x1 =   (-b + math.sqrt(disc)) / (2 * a)
        x2 =   (-b - math.sqrt(disc)) / (2 * a)
        print(f"The roots are real and different: {x1}, {x2}")
    elif disc < 0:
        real = -b / (2 * a)
        img = math.sqrt(-disc) / (2 * a)
        print(f"The roots are complex and different: {real} +i {img} and {real} -i {img}")

elif opt == '6':
    print("\n---- FACTORIALS ----")
    
    def find_factorial(n):
        n_factor = 1
        for i in range(1, n+1):
           i += 1
           n_factor *= i
           if i == n:
               print(f"\n{n} factorial = {n_factor}")  
               exit()   

        return n_factor    

    n = int(input("Enter the number n: ")) 
    print(find_factorial(n))
          
else:
    print("Invalid Input")           