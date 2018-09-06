import random
from Card import Card


class Deck:    
    def __init__(self):
        self.cards = []        

    def Create_Deck(self):
        for type in Card.card_type:
            for card in Card.cards:
                self.cards.append([card, type])
        Deck.Shuffle               

    def Shuffle(self):
        to_shuffle = []
        for position in range (0, len(self.cards)):
            picked = random.choice(self.cards)
            to_shuffle.append(picked)
            self.cards.remove(picked)
        self.cards = to_shuffle
    
    def Create_Shuffle_Deck(self):
        self.Create_Deck()
        self.Shuffle()
    
    def Amount_Left(self):
        return len(self.cards)
    
    def Deal_Card(self):
        return self.cards.pop(0)