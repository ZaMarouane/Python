"""
name = input("Enter your name:\n")
if name:
     print(f"Hello, {name}")
else:
    print("You forgot to enter your name")
"""

fruit_basket = ["Apples", "Oranges", "Bananas"]
guess = input("Guess the name of the fruits in the my basket: ").capitalize()

if guess in fruit_basket:
    print("Good guess")
else:
    print('Sorry, better luck next time')
