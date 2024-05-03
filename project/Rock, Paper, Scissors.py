import random
#Save ascii in a variables
rock_ascii = """
_      ___ _______
|  _,-' _ `\______)
|~'    ' `\()
|       (____)
|      (_____)
|--.____(___)

Rock
"""
paper_ascii = """
   ________.-.                .-.________
  (_______( / \----      ----/ \ )_______)
     (___()\)  )            (  (/()___)
      (__()                      ()__)
       (_()___/----      ----\___()_)  
   Paper
"""
scissor_ascii = """
     _
               _  / |
              / \ | | /\
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
     Scissor    |     |

"""
print("\nWelcome to Rock, Paper, Scissors game:")

confirm = input("Press enter to continue or type (Help) for the rule").lower()

if confirm == "help":
    print("""
          ********* RULES *********
          1) You choose and the computer choose
          2) Rock smaches Scissors -> Rock wins
          3) Scissors cut Paper -> Siccors win
          4) Paper covers Rock -> Paper wins
          """)

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice not in ["rock", "paper", "scissors"]:
          print("Invalid choice. Please run the program again and choose a rock, paper, scissors.")

#display user choice in ascii
else:
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose \n{scissor_ascii}")
        
    #computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if computer_choice == "rock":
        print(f"\nComputer chose:\n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"\nComputer chose:\n{paper_ascii}")
    else:
        print(f"\nComputer chose \n{scissors}")
        
# Determin the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or
    (user_choice == "paper" and computer_choice == "rock")
    or
    (user_choice == "scissors" and computer_choice == "paper")):
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"Computer wins! {computer_choice} beats {user_choice}.")
