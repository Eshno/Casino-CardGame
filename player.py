class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
    
    def showCards(self):
        for card in self.cards:
            print card.type , card.number
    
    def receiveCard(self, card):
        self.cards.append(card)