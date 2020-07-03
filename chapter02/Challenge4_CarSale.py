# Chapter 2, Challenge 4
# Write a Car Salesman program where the user enters the base price of a car.
# The program should add on a bunch of extra fees such as tax, license, dealer
# prep, and destination charge. Make tax and license a percent of the base price.
# The other fees should be set values. Display the actual price of the car once
# all the extras are applied

# Request base vehicle price
base = int(input("How much is the base price for the vehicle you want to buy?\n"))

# Define fixed costs
prep = 500
dest_charge = 200


# Calculate proportional costs
tax = base*0.20
lic = base*0.05

# Calculate total cost
total = base + prep + dest_charge + tax + lic

# Present tip optoins back to user
print("The base price of the vehicle is:", base, \
      "\nThe take home price is:", total)

input("\n\nPress Enter key to exit.")
