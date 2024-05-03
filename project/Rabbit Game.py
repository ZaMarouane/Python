print("Welcome to place the rabbit")
field = [['tree', 'tree', 'tree'], ['tree', 'tree', 'tree'], ['tree', 'tree', 'tree']]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere should the rabbit go?")
position = input('Please choose a row and a colom: ')
row = int(position[0])
column = int(position[1])

field[row-1][column-1] = "Rabbit"

print(" Success ...")

print(f"{field[0]} \n{field[1]} \n{field[2]}")
