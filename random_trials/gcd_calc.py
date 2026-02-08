#Finding the GCD of two numbers

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    #return a if b == 0 else gcd(b, a % b)
print("Given gdc(a, b)")    
a = int(input("a: "))
b = int(input("b: "))
print(f"gcd({a},{b}) = {gcd(a, b)}")
