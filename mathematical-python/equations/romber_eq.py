import math
from decimal import Decimal, ROUND_HALF_UP

def r4(x):
    return float(Decimal(str(x)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))

def f(x):
    return 14*x*math.exp(-x)

a,b=0,1

def trapezium(n):
    hs=(b-a)/n
    xs=[a+i*hs for i in range(n+1)]
    fs=[r4(f(x)) for x in xs]
    total=fs[0]+fs[-1]+2*sum(fs[1:-1])
    return r4(hs/2*total)

I0 = [trapezium(n) for n in (1,2,4,8)]
print('I0(h), I0(h/2), I0(h/4), I0(h/8) =', I0)

def romberg(coarse,fine,k):
    factor=4**k
    return r4((factor*fine-coarse)/(factor-1))

I1 = [romberg(I0[i],I0[i+1],1) for i in range(3)]
print('I1(h), I1(h/2), I1(h/4) =', I1)

I2 = [romberg(I1[i],I1[i+1],2) for i in range(2)]
print('I2(h), I2(h/2) =', I2)

I3 = romberg(I2[0],I2[1],3)
print('I3(h) =', I3)