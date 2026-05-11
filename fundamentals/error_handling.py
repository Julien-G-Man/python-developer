def __try__(x: int):
    try:  
        print("You entered:", int(x))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
x = input("Enter a number: ")  
if __name__ == "__main__":
    __try__(x)