# Challenge 1
# Create a program that prints a list of words in random order. The program
# should print all the words and not repeat any.

# imports
import random

# create list of random words
WORDS = ["Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye", "Captain America",\
         "War Machine", "Vision", "Scarlet Witch", "Ant-Man", "Spider-Man",\
         "Black Panther", "Captain Marvel", "Doctor Strange"]

# create a copy of the list the act as options
remaining = WORDS[:]

# create blank list of chosen words
chosen =[]

# Main code

# Loop through list of words while there are still words in the 'remaining' list
while remaining:
    word = random.choice(remaining)
    # add word to list of chosen words. Note if you use += here it will add the
    # strings element wise i.e. 'B,'l','a','c','k',' ','W','i','d','o','w' not
    # 'Black Widow'
    chosen.append(word)
    # remove word from remaining list
    remaining.remove(word)

print("Hello. Here's a list of random marvel heroes:")
print(chosen)

input("Press Enter to exit")
    
