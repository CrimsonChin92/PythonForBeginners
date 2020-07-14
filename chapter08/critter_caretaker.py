# Critter Caretaker 2.0
# A virtual pet to care for

# v2.0 - Allow user to specify amount of food and how long to play for. These affect the rate at which hunger and
#        boredom levels drop. A new function called boundary() has been added which repeats a quantity call,
#        when input is out of a given range. Print  outs in the class methods confirm user inputs and a prompt
#        if they reach saturation points.

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            # add choice for amount of food
            food = int(input("Feeding time. How much food would you like to give " + crit.name +"?" + \
                         "\nEnter a number between 0 and 10: "))
            # set boundaries to limit food
            food = boundary(quantity = food, lower = 0, upper = 10)
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
            crit.play(fun = fun)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
