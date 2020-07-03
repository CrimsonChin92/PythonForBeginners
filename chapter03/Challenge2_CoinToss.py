# Challenge 2
# Write a program that flips a coin 100 times and then tells you the number of
# head and tails

# import 'random' library
import random

# Greet user
print("Welcome!\n\nI am going to flip a coin 100 times.",\
      "I wonder how many heads/tails I will get...")

# Initiate infinite counting loop, but break at 100 interations
count=0
num_h=0
num_t=0

# Prompt user to start
input("\n\nPress 'Enter' key to start the coin toss\n\n")

while count<100:
    # generate a random 1 or 0 (heads or tails)
    coin=random.randrange(2)
    # increase the counter by one
    count += 1
    
    # if toss = 1 then add to heads count otherwise add to tails count
    if coin == 1:
        num_h += 1
        print("HEADS")
    elif coin == 0:
        num_t += 1
        print("TAILS")
        
    # add error catch break in case the random number generator fails
    else:
        print("The coin has landed on it's side. The game is broken. bye")
        break

# present results to user
print("\n\n",count,"coin tosses complete:",num_h,"heads and",num_t,"tails.")

# prompt user to exit
input("\n\nPress enter to exit")
        
    
