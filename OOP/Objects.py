class Fruit:
   def __init__(self, name, colour, is_edible):
      self.name = name
      self.colour = colour
      self.is_edible = is_edible

   def details(self): 
      print(f"My {self.name} is {self.colour}.")   
      
      if self.is_edible:
         print(f"The {self.colour} {self.name} is edible.")
      elif self.is_edible == None:
         print("You did not give me an appriate answer, I'm no sure whether it's edible or not.")
      else:
         print(f"The {self.colour} {self.name} is not edible.")  
         
            
fruit_name = input("Enter the name of a fruit: ")
fruit_color = input("Enter its color: ")
edible = input("Is it edible? (yes/no): ").lower()

if edible == "yes":
   is_edible = True
elif edible == "no":
     is_edible = False
else:
   is_edible = None
   
print(" ")

fruit = Fruit(fruit_name, fruit_color, is_edible)
print(fruit.details()) 

#mango = Fruit("mango", "green", False)

