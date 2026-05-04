import math, statistics
from statistics import mean, stdev

numbers = [i for i in range(10)]
print(numbers)

def getAverage(numbers):
    average = sum(numbers) /len(numbers)
    return average

def getStandardDeviation(n):
    variance = 0
    for i in range(1, 10):
        variance += pow(i - n, 2)
        
    standard_deviation = pow(variance, 1/2)    
    return int(standard_deviation)

def getFactorial(n):
    if n < 0 or not int(n):
        print(f"Thenumber must be greater than 0")
        exit()
        
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact    

def main():
    average = getAverage(numbers)
    print(f"\nThe average is {average}")
    
    standard_deviation = getStandardDeviation(average)
    print(f"The standard deviation is {standard_deviation}")
    std_int = int(standard_deviation)
    
    factorial = getFactorial(std_int)
    print(f"The factorial of {standard_deviation} is {factorial}")


if __name__ == "__main__":
    main()