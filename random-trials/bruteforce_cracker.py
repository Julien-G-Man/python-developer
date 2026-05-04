# Password Cracker Using Brute Force Linear Search
password = input("Enter six digit password password: ")
for i in range(100000000000000):
    print(i)
    if i == int(password):        
        print("Password found! The password is ", i)
        
        break
    