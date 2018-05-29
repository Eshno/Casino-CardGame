from UpdatedDeck import Deck
from Cards import Card
from UpdatedPlayer import Player
from UpdatedMiddle import Middle

player_amt = input("Insert player amount: ")
players = []
deck = Deck()
middle = Middle()


def Create_Players():
    names = ["Roger", "Shanon", "Carlo", "Carlos"]
    for p in range(0, player_amt):
        players.append(None)
        players[p] = Player(names[p] , [] , [], 0, False)

deck.Create_Deck()
deck.Shuffle()
Create_Players()
print middle.cards
