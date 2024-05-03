import random

#Greeting the user
print("Welcome to the coin Guessing game!")
#Choose a method to toss the coin
print("Choose a method to toss the coin:\n1. Using random.random()\n2. Using random.randin()")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    random_number = random.randint(0,1)
    if random_number == 0:
        computer_result = "Heads"
    else:
        computer_result = "Tails"

elif choice == "2":
    random_number = random.random()
    if random_number >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"

else:
    print("Invalid Choice. Please select either 1 or 2.")
    
user_choice = input("Enter your Guess (Heads or Tails):")

if user_choice.lower() == computer_result.lower():
    print("Congratilations! You won!")
else:
    print("Sorry, You lost!")

print(f"the computer's coin toss result was: {computer_result}")
    


