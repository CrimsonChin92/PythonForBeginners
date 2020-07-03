# Challenge 3
# Write a 'Who's Your Daddy?' program that lets the user enter the name of a
# male and produces the name of his father. (You can use celebrities, fictional
# characters, or even historical figures for fun.) Allow the user to add,
# replace, and delete son-father pairs.

# create dictionary of father-child pairs
fathers = {"Harry":"James","Ron":"Arthur","Draco":"Lucius","Dudley":"Vernon"}

# initialise value at choice == 1 - find a father
choice = "1"

# Greet user
print(
    """
                            "Who's Your Daddy?"

    Find out the father of your favourite Harry Potter characters. 
    If someone is missing. Feel free to add them to the reference list.

    """
    )

while choice != "0":
    
    if choice == "1":
        child = input("\nWho's father would you like to find out? ")
        child = child.capitalize()
        # find father in list if not present prompt user to try adding them
        father = fathers.get(child,"NA")
        if father == "NA":
            print("\nSorry I couldn't find",child,"in the list. "+\
                  "Feel free to add them to the list.")
        else:
            print("\nOK so I have checked and",child+"'s father is:",father)
            
    elif choice == "2":
        print("\nSo you think you know more than me?",\
              "Fine, add a new father-child combination.")
        # get key and value from user
        child = input("Child: ")
        child = child.capitalize()
        # check the name doesn't already exist in the list before proceding and ask user what to do if it does
        if child in fathers:
            update = input("This child already has a father, do you want to change it? ")
            update = update.upper()
            # if already exists set new to no
            new = "NO"
            
        else:
            new = "YES"

        # if user has asked to update or add to dictionary
        if new == "YES":
            father = input("Father: ")
            father = father.capitalize()
            print("\nAdding father of", child,":",father)
            fathers[child] = father
        elif update == "YES":
            father = input("Father: ")
            father = father.capitalize()
            print("\nUpdating father of", child,"from",fathers[child],"to",father)
            fathers[child] = father
        else:
            print("\nFather of", child, "has not been updated.")
            
    elif choice == "3":
        print("\nSo you want to break up a family?",\
              "Fine, remove a father-child combination.")
        child = input("\nWhat is the child's name? ")
        child = child.capitalize()
        # find father in list if not present prompt user to try adding them
        father = fathers.get(child,"NA")
        if father == "NA":
            print("\nSorry I couldn't find",child,"in the list. "+\
                  "Perhaps you already removed them.")
        else:
            print("\nOK so I'll remove the pair of",child,"and",father)
            del fathers[child]
        
    else:
        print("\n---Invalid selection made---")

    # present choice to user as what to do next time round
    choice = input("\n---\nWhat would you like to do next?" + \
               "\n 0 - Exit program. I Have what I need" + \
               "\n 1 - Find out someone's father" + \
               "\n 2 - Add/update a character's father" + \
               "\n 3 - Delete a father-child pair" + \
               "\n\n")

# user has chosen to exit
print("Thanks for using my reference guide.")
input("\n\nPress 'Enter' key to exit")
