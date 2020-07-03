# Chapter 2, Challenge 3
# Write a Tipper program where the user enters a restaurant bill total. The program should then display two amounts:
# a 15% tip and a 20% tip

# Request bill total
total = int(input("How much was your food bill?"))

# Calculate tip amounts
tip15 = total*0.15
tip20 = total*0.2

# Present tip optoins back to user
print("For a 15% tip you will need to add £", tip15)
print("For a 20% tip you will need to add £", tip20)

input("\n\nPress Enter key to exit.")
