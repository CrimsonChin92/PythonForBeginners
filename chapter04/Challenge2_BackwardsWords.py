# Challenge 2
# Create a program that gets a message from the user and then prints it out
# backwards

# Welcome user
print("Hello.\nDid you know it's backwards day today?")

# request message
message = input("Write a message to me and I'll prove it.\nMessage: ")

# cycle through from the end to the begining. Note the '+1' on the string length to ensure the referencing goes
# past the first character
for i in range(-1,-1*(len(message)+1),-1):
    print(message[i],end="")

input("\n\n!yad sdrawkcab saw ti uoy dlot I ,eeS\n\ntixe ot yek 'retnE' sserP")
