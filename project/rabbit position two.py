print("Welcome to rabbit position game!")
field = [["Rabbit", "Rabbit", "Rabbit"], ["Rabbit", "Rabbit", "Rabbit"], ["Rabbit", "Rabbit", "Rabbit"]]

print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("Where should the rabbit go?")
position = input("Please enter a row and a column: ")

row = int(position[0])
column = int(position[1])

field [row-1][column-1] = "Lion"
print(f"{field[0]} \n{field[1]} \n{field[2]}")
