def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)
   
n = 5   
if __name__ == "__main__":
    print(factorial(n))