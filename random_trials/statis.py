import statistics
from statistics import mean, median, mode,  stdev, variance


def find_factorial(n):
   if n < 0 or not int(n):
      print("n must be and an integer >= 0")
      exit()
      
   n_factor = 1
   for i in range(1, n+1):
      n_factor *= i
      if i == n:
         print(f"{n} factorial = {n_factor}")
         exit()   

   return f"{n} factorial = {n_factor}" 


def main():
    numbers = [i for i in range(1, 11)]
    print(numbers)

    the_mean = mean(numbers)
    print(f"Mean: {the_mean}")

    var = variance(numbers)
    print(f"Variance: {var}")
    
    stndev = stdev(numbers)
    print(f"Standard deviation: {stndev}")

    intStdev = int(stndev)
    print(f"Rounded standard deviation: {intStdev}")
    
    factorial = find_factorial(intStdev)
    print(factorial)
    
if __name__ == "__main__":    
    main()