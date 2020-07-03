# Challenge 4
# Create a game where he computer picks a random word and the player has to
# guess that word. The computer tells the player how many letters are in the
# word. The player then gets five chances to ask if a letter is in the word.
# The computer can only respond with "yes" or "no". Then, the player must guess
# the word.

# Import random library
import random

# Create list of words
WORDS = ("Apple", "Orange", "Pear", "Banana", "Mango", "Lemon", "Melon", \
         "Grape", "Plum", "Passionfruit", "Lime")

# Select word at random from list
word = random.choice(WORDS)

# Create new variable and assign the correct answer to it
correct = word

# create blank strings for the user to populate with guesses and correct letters
guesses = ""
letters = ""

# Greet user and introduce the game
print(
    """
                        Hello!

    Welcome to my game. It's called: 'Guess the word'.

    The rules are simple:

    1. I will think of a word and tell you how many letters it contains
    2. You have 5 attempts to find letters that are in this word
    3. You then have to guess the word based on the information you have

    """)

input("Are you ready to play?")

print("\nThe word I have chosen contains", str(len(correct)), "letters. \n")

for i in range(5):
    letter=input("\nGuess a letter: ")
    if letter.lower() in guesses:
        print("You already tried that one! What a waste of a guess.")
    elif letter.lower() in correct.lower():
        # add to array
        letters += (letter+", ")
        print("Yes, the letter", letter, "is in the word")
    else:
        print("No, the letter", letter, "is not in the word")

    # add guess to array of guesses
    guesses += (letter.lower()+", ")

    # present current situation to user
    print("So far you have had", i+1, "guesses and know the word contains: ", end="")
    if letters:
        print(letters)
    else:
        print("No correct guesses made")

# Prompt user to make a guess at the word
word = input("\n\nYou've had 5 guesses, what is the word I'm thinking of? ")

if word.lower() == correct.lower():
    print("Congratulations! You guessed my word. It was: ", end="")
else:
    print("Sorry, the word i was thinking of was actually: ", end="")

print(correct)

input("\n\nThanks for playing. Press 'Enter' to exit.")
