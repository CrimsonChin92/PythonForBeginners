# Challenge 4
# The player and computer trade places.
# The player picks a random number between 1 and 100 that the computer has to
# guess.

import random

# Computer prompts user to select a number between 1 and 100
print("Hello. Let's play a game.")
print("Think of a number between 1 and 100, and I'll try to guess it.\n")

# Computer asks how many attempts he gets
max_tries = int(input("OK, got a number? How many attempts can I have to get it?"))

# set the initial values
max_guess = 100
min_guess = 1
tries = 0

# guessing loop
# loop until max number of tries is reached
while tries < max_tries:
    # computer guesses based on upper/lower limits
    guess=random.randint(min_guess, max_guess)
    tries += 1
    correct=input("\nIs it "+str(guess)+"? (y/n)")
    if correct.lower() == "y":
        print("\nWoohoo! I guessed it! The number was", guess,\
               "And it only took me", tries, "tries!\n")
        break
    elif  correct.lower() == "n":
        limit = input("\nDamn! Is it higher or lower than my guess? (h/l)")
        # update random bounds based on previous guess
        if limit.lower() == "h":
            min_guess = guess + 1
        elif limit.lower() == "l":
            max_guess = guess - 1
        else:
            print("\nWell if it's not higher or lower, I must be right!")
            break
    else:
        print("\nYou're not playing fair. I don't want to play anymore")
        break

if correct.lower() != "y" and tries >= max_tries:
    number = int(input("\nDoh! Guess you win this round. What was the number?"))
    if number > guess:
        diff = number - guess
    else:
        diff = guess - number
    print("I was only", diff, "away!")


input("\n\nPress the enter key to exit.")
