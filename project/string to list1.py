"""
names_string = input("Enter names separated by comma ..")
names = names_string.split(", ")
print(type(names))
print(names)
"""
'''import random

print("Welcome to 'whose wallet?'")
print("You'll give me a list of name, an I'll pick a person to pay")
names = input("If you are ready, enter the names separated with comma: ")

names_list = names.split(", ")
names_len = len(names_list)
lenght = names_len - 1

random_number = random.randint(0,names_len-1)
random_person = names_list[random_number]
print(f"Please ask ' {names_list[random_number]} ' to take his wallet out. Dinner is on him")
'''

"""import random

print("Welcome to 'whose wallet?'")
print("You'll give me a list of name, an I'll pick a person to pay")
names = input("If you are ready, enter the names separated with comma: ").split(", ")
print(f"Please ask {random.choice(names) } to take his wallet out, dinner on him")
"""

import random

print("Welcome to 'whose wallet?' \nYou'll give me a list of name, an I'll pick a person to pay")
print(f"Please ask {random.choice(input ('Enter the names separated with comma: ').split(', ')) } to take his wallet out, dinner on him")




