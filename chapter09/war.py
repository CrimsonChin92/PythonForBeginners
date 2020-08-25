# War
# From 1 to 7 players compete against a dealer. Highest card wins.

import cards, games

class WAR_Card(cards.Card):
    """ A card for the game WAR."""

    @property
    def value(self):
        v = WAR_Card.RANKS.index(self.rank) + 1
        if v == 1: # set value of ace to be higher than king
            v = 14

        return v

class WAR_Deck(cards.Deck):
    """ A War deck. """
    def populate(self):
        for suit in WAR_Card.SUITS: 
            for rank in WAR_Card.RANKS: 
                self.cards.append(WAR_Card(rank, suit))

    @property
    def cards_remaining(self):
        tot = len(self.cards)
        return tot

class WAR_Hand(cards.Hand):
    """ A hand of cards for the game WAR. """
    def __init__(self, name):
        super(WAR_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(WAR_Hand, self).__str__()  
        if self.value_hand:
            rep += "(" + str(self.value_hand) + ")"        
        return rep

    @property
    def value_hand(self):
        for card in self.cards:
            val = card.value
            return val
            

class WAR_Game(object):
    """ A War Game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = WAR_Hand(name)
            self.players.append(player)

        self.dealer = WAR_Hand("Dealer")

        self.deck = WAR_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # deal 1 card to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 1)
        for player in self.players:
            print(player)
        print(self.dealer)

        # Determine highest player score
        max_score = 0
        for player in self.players:
            if max_score < player.value_hand:
                max_score = player.value_hand

        # Determine winner(s)
        winners = []
        if self.dealer.value_hand >= max_score:
            winners.append(self.dealer)
        else:
            for player in self.players:
                if max_score == player.value_hand:
                    winners.append(player)

        print("\nThe winner(s):")
        for winner in winners:
            print(winner)

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("/t/tWelcome to WAR!\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ").title()
        while name in names:
            name = input("Player '" + name + "' already exists. Try a different name: ").title()
        names.append(name)
    print()

    game = WAR_Game(names)

    again = None
    while again != "n":
        if game.deck.cards_remaining < number:
            # if low on cards reset deck
            input("\nLow on cards. Press enter to reset deck\n")
            game.deck.populate()
            game.deck.shuffle()   
        
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")

    
