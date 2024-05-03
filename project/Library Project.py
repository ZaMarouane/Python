'''# create empty list
library = []
#ask the user to enter a book he or she has
first_book = input("Enter the name of a book you own: ") 
second_book = input("Enter another name of a book you own (or press 'Enter' to Skip): ")
#add those books to the empty list
library.append(first_book)
library.append(second_book)
print("\n")
#print the the boor are in the library
print(f"Your Library: {library}")

print("\n")
# create empty list for wishlist book
wish_list = []  
#ask the user to enter a book he or she wich to buy
wish_list1 = input("Enter the name of book you wish to have in the future: ")
wish_list2 = input("Enter another book you wish to have (or press'Enter to Skip): ")

#add those books to the empty list
wish_list.append(wish_list1)
wish_list.append(wish_list2)
print("\n")
#print the books are in the wishlist
print(f"Your Wishlist: {wish_list}")

print("\n")
# create empty list for the acquired book
acquired = []
acquired_book = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to Skip): ")
acquired.append(acquired_book)
#print the books have been acquired
print(acquired)
print(wish_list)
#Add the aquired book to the library
updated_library = (library + acquired)
#Remove the aquired book from the wishlist
updated_wishlist = wish_list.remove(acquired_book)
print("\n")

#print the new library and the wishlist
print(f"Updated Library: {updated_library}")
print(f"Updated Wishlist: {updated_wishlist}")

# create empty list for the donate book
donate = []
donate_book = input ("Enter the name of the book from your library you wish to donate (or press 'Enter to Skip):")

# print the final list after donations
final_library = updated_library.remove(donate_book)
print(f"The final library after donations: {final_library}")

'''

# step 1: setup
library = []
wishlist = []

# step 2: Adding individual books
book_name = input("Enter the name of a book you own: ")
library.append(book_name)

book_name = input("Enter the name of another book you own (or press 'Enter' to Skip): ")

if book_name:
    library.append(book_name)

print("\nYour Library: ", library)

# step 3: Managing the wishlist
book_name = input("Enter the name of a book you own: ")
wishlist.append(book_name)

book_name = input("Enter the name of another book you own (or press 'Enter' to Skip): ")

if book_name:
    wishlist.append(book_name)

print("\nYour Library: ", library)

# step 4: Merging wishlist into library
acquired_book = input("\nEnter the name of a book from your wishlist that you've acquired (or press enter to skip): ")
if acquired_book in wishlist:
     library.append(acquired_book)
     wishlist.remove(acquired_book)

print("\nUpdated Library: ", library)
print("Updated Wishlist: ", wishlist)

# step 5: Donation books
donated_book = input("\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donated_book in library:
    library.remove(donated_book)

print("\nFinal Library after donations: ", library)


