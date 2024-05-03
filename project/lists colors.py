
colors = []
fav_color = input("Type the firt color you like: ")
colors.append(fav_color)
choice = input("Do you want to add more colors? Yes or No? ").lower()

if choice == "yes":
    fav_color = input("Add another color you like:")
    colors.append(fav_color)
    print("The colors you like are:")
    print(colors)

elif choice == "no":
    print("The color you like are:")
    print(colors)

else:
    print("Invalid choice, please type either Yes or No")
    
