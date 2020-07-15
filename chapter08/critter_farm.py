# Critter Farm

# A collection of virtual pets to care for

# Based on Critter Caretaker 3.0


import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        status = ("Critter status:\n")
        status += "Name:\t\t" + self.name + "\n"
        status += "Hunger:\t\t" + str(self.hunger) + "\n"
        status += "Boredom:\t" + str(self.boredom) + "\n"
        return status

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("\nGiving",self.name,food,"food")
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            print("Please...no more food! I'm stuffed!")
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("\nGiving",self.name,fun*10,"minutes of fun")
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            print("I'm exhausted! Let's play another time.")
            self.boredom = 0
        self.__pass_time()

def boundary(quantity, lower, upper):
    """Print error messages to user whilst quantity is outside of bounds"""
    in_range = False
    while not in_range:
        if quantity < lower or quantity > upper:
            quantity = int(input("That is out of range, please try a number between " + \
                                 str(lower) + " and " + str(upper) + ": "))
        else:
            in_range = True
            return quantity         


def main():

    # Critter 1
    crit_name = input("What do you want to name your first critter?: ")
    crit1 = Critter(name=crit_name,hunger=random.randint(0,10),boredom=random.randint(0,10))

    # Critter 2
    crit_name = input("What do you want to name your second critter?: ")
    crit2 = Critter(name=crit_name,hunger=random.randint(0,10),boredom=random.randint(0,10))

    # Critter 3
    crit_name = input("What do you want to name your third critter?: ")
    crit3 = Critter(name=crit_name,hunger=random.randint(0,10),boredom=random.randint(0,10))
    
    # create collection of critters
    critters = [crit1, crit2, crit3]

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            for crit in critters:
                crit.talk()
        
        # feed your critter
        elif choice == "2":
            # add choice for amount of food
            food = int(input("Feeding time. How much food would you like to give " + crit.name +"?" + \
                         "\nEnter a number between 0 and 10: "))
            # set boundaries to limit food
            food = boundary(quantity = food, lower = 0, upper = 10)
            for crit in critters:
                crit.eat(food = food)
         
        # play with your critter
        elif choice == "3":
            # add choice for duration of play
            play_time = int(input("Play time. How long do you want to play with " + crit.name +" for?" + \
                         "\nEnter a number of minutes: "))
            # set boundaries to limit play time
            play_time = boundary(quantity = play_time, lower = 0, upper = 60)
            # convert play time to score
            fun = play_time//10
            if play_time%10 >= 5: # round up
                fun += 1
            for crit in critters:
                crit.play(fun = fun)

        # check status with secret combination
        elif choice == "0123":
            for crit in critters:
                print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
