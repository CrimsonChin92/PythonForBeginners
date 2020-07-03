# Word Jumble 2.0
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

# v 2.0 includes hints for each word and a scoring system

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# ADDED: create hints for each word
HINTS = ("a type of snake", "a muddle", "simple", "hard", "the response to a question", "wooden piano")
# ADDED: generate random number for indexing arrays. Cannot use random.choice
# because we need to use the same index for both arrays
idx = random.randrange(len(WORDS))
# pick one word randomly from the sequence
word = WORDS[idx]
hint = HINTS[idx]
# create a variable to use later to see if the guess is correct
correct = word
# ADDED: create a variable to say whether or not the hint has been used
clue = ""

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    # ADDED ask for clue
    if clue.lower() != "yes":
        clue = input("Would you like a hint?")
        if clue.lower() == "yes":
            print("\nYour clue is:", hint)
    
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")

# ADDED: points given out based on the value of clue
if clue.lower() == "yes":
    print("You needed a clue though, so only 1 point.")
else:
    print("And you didn't even need a clue! 3 points!")
    
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
