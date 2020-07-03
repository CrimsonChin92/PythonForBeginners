# Guess My Number 4.0
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

# v 2.0 includes the addition of a max number of guesses and some sassy commentary 
# v 3.0 includes the ask_number function from chapter 6
# v 4.0 shifts programs code into a function called main()

import random

# ADDED ask_number function

def ask_number(question, low, high, step = 1): # added input for step and set default to 1
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step): # added step input which can be varied with function call
        print("Try a number between", low, "and", high) # user asks for number outside of range
        response = int(input(question))
    return response

def main():
    """Main code of guess muy number game."""
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    low = 1     # set lower bound, this will be updated by the while loop
    high = 100  # set upper bound, this will be updated by the while loop
    the_number = random.randint(1, 100)
    guess = ask_number("Take a guess: ",low,high) # changed from input function to ask_number function
    tries = 1
    max_tries = 10

    # guessing loop
    # loop until user guesses correctly or max number of tries is reached
    while guess != the_number and tries < max_tries:
        if guess > the_number:
            print("Lower...")
            high = guess    # player guesses high, change upper bound to players guess
        else:
            print("Higher...")
            low = guess     # player guesses low, change upper bound to players guess            

        guess = ask_number("Take a guess: ",low,high) # call ask_number() function
        tries += 1

    if guess == the_number:
        print("You guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!\n")
    else:
        print("You idiot! I gave you", max_tries, "tries and you couldn't guess it.")
        print("The number was obviously", the_number)

# call main function to run

main()  
input("\n\nPress the enter key to exit.")
