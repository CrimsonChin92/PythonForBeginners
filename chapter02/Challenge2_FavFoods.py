# Chapter 2, Challenge 2
# Write a program that allows the user to enter his or her two favourite foods.
# The program should then print out the name of a new food by joining the
# original food names together

# Request food names
food1 = input("What is your favourite food?\n")
food2 = input("What is your second favourite food?\n")

# concatenate strings and present them back to user
print("Then your ultimate food must be:", \
      food1 + food2.lower())

input("\n\nPress Enter key to exit.")
