# Challenge 4
# Improve the 'Who's Your Daddy?' program by adding a choice that lets the user
# enter a name and get back a grandparent. Your program should still only use one
# dictionary of son-father pairs. Make sure to include several generations in
# your dictionary so that a match can be found

# create dictionary of parent-child pairs
parents = {"ELIZABETH II":"GEORGE VI",
           "GEORGE VI":"GEORGE V", "EDWARD VIII":"GEORGE V",
           "GEORGE V":"EDWARD VII",
           "EDWARD VII":"VICTORIA",
           "VICTORIA":"EDWARD AUGUSTUS",
           "WILLIAM IV":"GEORGE III","GEORGE IV":"GEORGE III","EDWARD AUGUSTUS":"GEORGE III"
           }

# initialise values
choice = "1"
new = ["NO","NO"]
update = ["NO","NO"]
prompt = ("Parent: ", "Grandparent: ") 

# Greet user
print(
    """
                            "Who's Your Grandaddy"

    Enter an English Monarch and find out who their parent or grandparent is. 
    If someone is missing, feel free to add them to the reference list.

    """
    )

while choice != "0":

    if choice == "1":
        child = input("\nWho's parent would you like to find out? ")
        child = child.upper()
        # find parent in list if not present prompt user to try adding them
        parent = parents.get(child,"NA")
        if parent == "NA":
            print("\nSorry I couldn't find",child,"in the list. "+\
                  "Feel free to add them to the list.")
        else:
            print("\nOK so I have checked and",child+"'s parent is:",parent)
   
    elif choice == "2":
        child = input("\nWho's grandparent would you like to find out? ")
        child = child.upper()
        # find parent in list if not present prompt user to try adding them
        parent = parents.get(child,"NA")
        if parent == "NA":
            print("\nSorry I couldn't find",child,"in the list. "+\
                  "Feel free to add them to the list.")
        else:
            # find grandparent based on parents name
            grandparent = parents.get(parent,"NA")
            if grandparent == "NA":
                print("\nSorry I couldn't find",child+"'s grandparent in the list. "+\
                      "Feel free to add them to the list.")
            else:
                print("OK so I have checked and",child+"'s grandparent is:",grandparent)
            
    elif choice == "3":
        print("\nSo you think you know more than me?",\
              "Fine, add/update the lineage of a monarch.")
        # get key and value from user
        child = input("Monarch: ")
        child = child.upper()
        # check the name doesn't already exist in the list before proceding and ask user what to do if it does
        if child in parents:
            ans = input("\nThis monarch already has a parent, do you want to change it? ")
            update[0] = ans.upper()
            # if already exists set new to no
            new[0] = "NO"
            
            # check for granparent also
            parent=parents.get(child,"NA")
            if parent in parents:
                ans = input("\nThis monarch already has a grandparent, do you want to change it? ")
                update[1] = ans.upper()
                # if already exists set new to no
                new[1] = "NO"

            else:
                new[1] = "YES"
            
        else:
            new[0] = "YES"
            ans = input("\nNo parent for "+child+" has been found - you can add a new parent. "\
                        "Would you also like to add a grandparent? ")
            new[1] = ans.upper()

        # if user has asked to update or add to dictionary
        if "YES" not in new and "YES" not in update:
            print("\nLineage of", child, "has not been updated.")
            
        else:
            for i in range(2):
                if new[i] != "YES" and update[i] != "YES":
                    print(prompt[i], "of", child, "has not been changed.")

                else:
                    new_parent = input(prompt[i])
                    parent = new_parent.upper()

                    # tell the user what's going on
                    if new[i] == "YES":
                        print("\nAdding parent of", child,":",parent,"\n")
                    elif update[i] == "YES":
                        print("\nUpdating parent of", child,"from",parents[child],"to",parent,"\n")
                    else:
                        print("\n!\nError encountered check code for adding names")

                    # update names
                    parents[child] = parent
                
                # update child to be parent
                child = parent
                
        # reset new/update lists
        new = ["NO","NO"]
        update = ["NO","NO"]
            
    elif choice == "4":
        print("\nSo you want to break up a family?",\
              "Fine, remove a parent-child combination.")
        child = input("\nWhat is the Monarch's name? ")
        child = child.upper()
        # find parent in list
        parent = parents.get(child,"NA")
        if parent == "NA":
            print("\nSorry I couldn't find",child,"in the list. "+\
                  "Perhaps you already removed them.")
        else:
            print("\nOK so I'll remove the pair of",child,"and",parent)
            del parents[child]
        
    else:
        print("\n---Invalid selection made---")

    # present choice to user as what to do next time round
    choice = input("\n---\nWhat would you like to do next?" + \
               "\n 0 - Exit program. I Have what I need" + \
               "\n 1 - Find out someone's parent" + \
               "\n 2 - Find out someone's grandparent" + \
               "\n 3 - Add/update a Monarch's parent and/or grandparent" + \
               "\n 4 - Remove a Monarch's parent" + \
               "\n\n")

# user has chosen to exit
print("Thanks for using my reference guide.")
input("\n\nPress 'Enter' key to exit")
