# Guess My Number 2.0
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

# v 2.0 includes the addition of a max number of guesses and some sassy commentary 

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
max_tries = 10

# guessing loop
# loop until user guesses correctly or max number of tries is reached
while guess != the_number and tries < max_tries:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

if guess == the_number:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
else:
    print("You idiot! I gave you", max_tries, "tries and you couldn't guess it.")
    print("The number was obviously", the_number)
  
input("\n\nPress the enter key to exit.")
