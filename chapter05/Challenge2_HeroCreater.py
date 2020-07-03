# Challenge 2
# Write a Character Creater program for a role-playing game. The player should
# be given a pool of 30 points to spend on 4 attributes: Strength, Health,
# Wisdom, and Dexterity. The player should be able to spend points from the pool
# on any attribute and should be able to take points from an attirbute and put
# them back in the pool

# Initialise attribute array.
# using dictionary to allow the attributes to be referenced as keys
skills = {"STRENGTH": 0, "HEALTH": 0, "WISDOM": 0, "DEXTERITY": 0}

# Initialise skill points pool
pool = 30

# create blank parameter to signify the user is finished selecting points
finished = None 

# Introduce the hero creator
print(
    """
                    WELCOME 
                    -------
                    
            This is the hero creator
            
                       _ | 
                       M | 
                    /\-O-T 
                    \/ | 
                      / \ 

            Here you can create your
            hero by distributing skill
            points to the 4 attributes:

                Strength
                Health
                Wisdom
                Dexterity
            
    """
    )

input("Are you ready to get started?")

# while the user is not finished present options to user
while not finished:

    # print current points distribution
    print("\n\n-----\nYour hero currently has the following attributes:")
    print(skills)
            
    # present choices to user
    choice = input("\n\nYou have " + str(pool) + " points remining. " + \
                   "What would you like to do?" + \
                   "\n0 - Confirm points and exit" + \
                   "\n1 - Add skill points" + \
                   "\n2 - Remove skill Points" + "\n\n")
    
    # based on choice do one of two things
    if choice == "0":
        finished = 1

    elif choice == "1":
        skill = input("Which attribute would you like to add points to? ")
        skill = skill.upper()

        # prompt the user to try again until a valid name is entered
        while skill not in skills:
            skill=input("Attribute not found, please try another name: ")
            skill = skill.upper()
            
        # as soon as the selected attribute is valid ask user
        # how  many points to add
        points = int(input("\nHow many points would you like to add? "))
        # limit points to remainder in pool
        if points > pool:
            print("You don't have that many points remaining. Points limited")
            points = pool
        # update points in chosen attribute and pool
        skills[skill] += points
        pool -= points

        # clear skill name
        skill = ""

    elif choice == "2":
        skill = input("Which attribute would you like to remove points from? ")
        skill = skill.upper()
        # prompt the user to try again until a valid name is entered
        while skill not in skills:
            skill=input("Attribute not found, please try another name: ")
            skill = skill.upper()

        # if the selected attribute is valid ask user how many points to remove
        points = int(input("\nHow many points would you like to remove? "))
        # limit points to remainder in pool
        if points > skills[skill]:
            print("You cannot have negative points. Capped at zero")
            points = skills[skill]
        # update points in chosen attribute and pool
        skills[skill] -= points
        pool += points
        
        # clear skill name
        skill = ""

    else:
        print("Invalid choice made. Please try again.")

# Thank the user for creating a hero and prompt them to exit
print("\n\n-----\nSkill points confirmed. Your hero is ready to go on a quest.")
input("\n\nPress 'Enter' to exit")
