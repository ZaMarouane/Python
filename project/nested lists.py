
basket = [["Apples", "Bananas"], ["milk", "Water"]]
print(basket)
input("Press enter to change the content .....")
print("Here is the updated basket")
basket[0].insert(0, "Orange")
basket[0].insert(3, "Kiwis")
basket[1].insert(0, "Coffee")
basket[1].append("Tea")
basket.append([1, 2, 3])


for sublist in basket:
    if 'Water' in sublist:
        sublist.remove('Water')

print(basket)
