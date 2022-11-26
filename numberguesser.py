## Import module for random integer
import random
## User imputs
print("Hi Bella!")
x = int(input("What is the lowest number?"))
y = int(input("What is the highest number?"))
z = random.randint(x, y)
choice = int(input("Guess a number!"))
#While loop to check if the user choice is equal to random number
while choice != z:
#If choice is too high, ask if user wants to try again
   if choice > z:
       print("Too high")
       h = input("Want to try again?")
       if h == "Yes":
#Update choice variable
           choice = int(input("Guess a number!"))
#If no, exit loop          
       if h == "No":
           print("Have a nice day.")
           break
#If choice is too low, ask if user wants to try again
   if choice < z: 
       print("Too low")
       h = input("Want to try again?")
       if h == "Yes":
#Update choice variable
           choice = int(input("Guess a number!"))
       if h == "No":
           print("Have a nice day.")
           break
#If user choice is equal to random number, exit loop
   if choice == z:
       print("You got it!")
       break
