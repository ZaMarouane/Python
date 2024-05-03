#Game

print("Welcome to my city")
print("There are two city (Sale), or (Rabat)")
city = input("Which city you want to go to?\n")
if city.lower() == "sale":
    print("There's no train to Sale today\nWaint untill tomorrow")

elif city.lower() == "rabat":
    print("Welcome to the that is going to Rabat")
    station = input("Which station you'ar going to, (Rabat Agdal), or (Rabat City)")
    if station.lower() == "rabat agdal":
        print("Good we'll be in Rabat Agdal for about two hours")
        door = input("Which door you want to go out from, (Right) ro (Left)")
        if door.lower() == "right":
            print("This do leads to the ocean Atlantic")
        elif door.lower() == "left":
            print("This door leads to the avenue of Embassies of UAE, NETHERLAND, KSA, and NEW ZELAND")
            print("Game over")
        else:
            print("Invalid input")
            
else:
    print("invalid input")


