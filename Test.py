from Deck import Deck
from Player import Player

someobj = []
Deck.Create_Deck(someobj)
Deck.Shuffle_Deck(someobj)




player1 = Player("Carlo" , [] , [], 0)
player2 = Player("Carol" , [] , [], 0)
player3 = Player("Mellie" , [] , [], 0)
player4 = Player("Sara" , [] , [], 0)


for i in range(0,4):
    player1.cards.append(Deck.deal_card(someobj))
    player2.cards.append(Deck.deal_card(someobj))
    player3.cards.append(Deck.deal_card(someobj))
    player4.cards.append(Deck.deal_card(someobj))
    


print player1.cards
print player2.cards
print player3.cards
print player4.cards

