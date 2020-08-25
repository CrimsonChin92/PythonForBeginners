# Explorer
# Players travel around a land from location to location

import games,random

class Explorer_player(object):
    """ A player in the explorer game """

    def __init__(self, name, location = "Sea"):
        self.name = name
        self.location = location

        print(self.name,"has landed in",self.location)

    def __str__(self):
        rep = self.name.title() + " is in "
        rep += self.location
        return rep

    def travel(self, destination):
        if destination == "Sea":
            print(self.name, "is setting sail.")
        elif self.location == "Sea":
            print("Land ho!",self.name,"is making port.")
        else:
            print(self.name, "is crossing the border from", self.location,
                  "to",destination)
        self.location = destination

class Explorer_place(object):
    """ A location in the explorer game """

    def __init__(self,location,borders):
        self.location = location
        self.borders = borders

    def __str__(self):
        rep = self.name + "has borders with:"
        rep += self.borders
        return rep

class Explorer_game(object):
    """ A game of explorer """

    # define list of places and their borders
    locations = {"Australian Capital Territory":
                 ["New South Wales"],
                 "New South Wales":
                 ["Australian Capital Territory","Queensland","South Australia","Victoria","Sea"],
                 "Northern Territory":
                 ["Queensland","South Australia","Western Australia","Sea"],
                 "Queensland":
                 ["New South Wales","Northern Territory","South Australia","Sea"],
                 "South Australia":
                 ["New South Wales","Northern Territory","Queensland","Victoria","Western Australia","Sea"],
                 "Tasmania":
                 ["Sea"],
                 "Victoria":
                 ["New South Wales","South Australia","Sea"],
                 "Western Australia":
                 ["Northern Territory","South Australia","Sea"],                 
                 "Sea":
                 ["New South Wales","Northern Territory","Queensland","South Australia","Tasmania","Victoria","Western Australia"]}

    def __init__(self,names):

        # create place objects for every loaction
        self.places = []
        for item in self.locations.items():
            location = item[0]
            borders = item[1]
            place = Explorer_place(location, borders)
            self.places.append(place)

        # create player objects for everyone playing    
        self.players = []
        for name in names:
            place = random.choice(self.places)
            location = place.location
            player = Explorer_player(name, location)
            self.players.append(player)
        

    def instructions(self, player):
        print("\n" + player.name, "you are currently in", player.location, end=".")
        print("""
What will you do next?

0 - Do nothing, I quite like it here
1 - Move elsewhere, I'm fed up with this place
2 - Leave this world entirely never to return
3 - End game! we've all stopped having fun
""")

    def play(self):
        """ Play the game """
        choice = None
        # Loop through the players until someone ecits the game
        while choice != 3:
            if not self.players:
                print("There is noone left, the game is ending.")
                break
            for player in self.players:
                self.instructions(player)
                choice = games.ask_number("Choice: ", 0, 4)
                if choice == 0:
                    print("\nHave it your way. Stay in rubbish", player.location)
                elif choice == 1:
                    self.move(player)
                elif choice == 2:
                    print("\n" + player.name, "is outta here!")
                    self.players.remove(player)
                else:
                    print("Looks like someone is bored. Let's just end it there.")    
                    break

    def move(self,player):
        """ move player to a different location """
        for place in self.places:
            if place.location == player.location:
                destinations = place.borders
                print("\nYou can move to any of the following destinations:")
                n = 1
                for i in destinations:
                    print(str(n),"-",i)
                    n += 1
        choice = games.ask_number("\nChoice: ", 1, len(destinations)+1)
        destination = destinations[choice-1]
        player.travel(destination)                                    
        
    
def main():
    print("\t\tWelcome to Explorer!\n")
    
    names = []
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ").title()
        while name in names:
            name = input("Player '" + name + "' already exists. Try a different name: ").title()
        names.append(name)
    print()
 
    game = Explorer_game(names)
    game.play()

    # present final results
    print("\nFinal positions:")
    for player in game.players:
        print(player.name, ": " + player.location)

    
main()
input("\n\nPress the enter key to exit.")
