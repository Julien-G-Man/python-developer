# Dice Rolling Game
import random

def play():
   print("Hello, welcome to the Dice Roller Game!")
   user = input("Enter your name: ")
   computer = "Roblox"
   print(f"\nHello {user}, you'll be playing against {computer}.")
   print("The rules are simple, just roll the dice and whoever has the highest score after five attempts is the winner.")
   return roll(user, computer)

def roll(user, computer):
   options = [1, 2, 3, 4, 5, 6]
   user_score = 0
   computer_score = 0  
   p = 0
      
   result = [
      {'name': user, 'score': user_score},
      {'name': computer, 'score': computer_score}
   ]
   
   for attempt in range(5):
      print(f"\nRound {attempt + 1}")
      user_choice = input ("Press r to roll, or q to quit >>> ")
      
      if user_choice == ('r' or ''): 
         attempt += 1 
         user_roll = random.choice(options)
         computer_roll = random.choice(options)
           
         print(f"{user}: {user_roll}")  
         print(f"{computer}: {computer_roll}")
         
         if user_roll > computer_roll:
            print(f"\n{user} wins!")
         elif user_roll == computer_roll:
            print(f"It's a tie!")
         else:
            print(f"\n{computer} wins!") 
          
         user_score += user_roll
         computer_score += computer_roll  
         
         print(f"{user}: {user_score}, {computer}: {computer_score}")
         
      elif user_choice == "q":
         print("Quitting...")
         break # stop iteration and give final result
      else:
         print("Invalid input!") 
         continue
      
   print("\nFinal Results")   
   print(f"{user}: {user_score}")
   print(f"{computer}: {computer_score}")
   
   result[0]["score"] = user_score
   result[1]["score"] = computer_score
   
   if user_score > computer_score:
      print(f"\n{user} wins!\nYou're a damn beast.")
   elif user_score == computer_score:
      print(f"\nIt's a tie!")
   else:
      print(f"\n{computer} wins! \nYou just got defeated.") 
      
   return result

if __name__ == "__main__":
   play()