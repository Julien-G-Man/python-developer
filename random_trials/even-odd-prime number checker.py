# Even/odd and prime number checker
number = int(input("Enter a number: "))
if number%2 == 0:
    print(number, " is even")
else:
    print(number, " is odd")

# checking if number is prime
for i in range(2, number):
    if number % i == 0:
        print(number, " is not prime")
        break
    else:
#        for i in range(1, 1000000):
#            print(i)
        print(number, " is prime")
        break

