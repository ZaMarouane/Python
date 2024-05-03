#Game

print ( "☠")
print ( "Welcome to my island!" )   #show welcome message
print ( "There are two doors in front of you. 🧧 a red door and 🟦 a blue door" )
door = input ( "Which one you want?\n" ) #ask the user to chose a door

if door.lower() == "red":           #check if the color he entered is red
    print ( "Oops! You chose the crocodile door.\nGame over! 🐊 🐊 🐊" )

elif door.lower() == "blue":        #check if the color he entered is blue
    print ( "You found three boxes, 🎁 White, 🎁 Black, 🎁 Green" )
    box = input ("Which box you want to opend?\n").lower() ##ask the user to chose a door
    if box == "white":              #check if the color he entered is white
        print ("Oops! You opened a box filled with snakes 🐍🐍🐍")
    elif box == "black":            #check if the color he entered is black
        print ("Oops! You opened a box filled with spiders 🕷 🕸 🕷")
    elif box == "green":            #check if the color he entered is green
        print ("Congratulations! You found the treasure!")
    else:
        print ("Invalid Choice! 🙈🙈🙈")

else:
    print ("Invalid Choice! 🙈🙈🙈")
    
    
