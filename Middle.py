from UpdatedDeck import Deck

class Middle:
    def __init__(self):
        self.cards = []
    
    def Show_Middle(self):
        for card in self.cards:
            print card
    
    def Get_Card(self, card):
        self.cards.append(card)

