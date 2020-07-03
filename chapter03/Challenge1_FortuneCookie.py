# Challenge 1: Write a program that simulates a fortune cookie. The program
# should display one of five unique fortunes, at random, each time it's run

# Import 'random' library to be used to determine fortune
import random

# Welcome user
print("Hello. Welcome to the fortune cookie generator.\n\n")

# Generate random number between 1 and 5
number = random.randint(1,5)

print("Here is your fortune...\n")

# Select fortune based on number generated
if number == 1:
    print("You will become rich one day...not Bill Gates rich, but maybe Peter Andre rich.")

elif number == 2:
    print("Today is a bad day. Just go back to bed.")

elif number == 3:
    print("Is a fortune cookie even a cookie? False advertising!")

elif number == 4:
    print("Help! I'm stuck in a fortune cookie factory")

elif number == 5:
    print("Looks like your stars are aligned. Take a chance and see what happens.",\
          "It could be the best decision you ever make.")

else:
    print("I think your fortune cookie is broken")

input("\n\nThat's all. Pree 'Enter' key to exit")
