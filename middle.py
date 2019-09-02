class Middle:
    def __init__(self):
        self.cards = []
    
    def showMiddle(self):
        for card in self.cards:
            print(card.name, card.type, ' | ')
    
    def receiveCard(self, card):
        self.cards.append(card)
    
    def giveCard(self, pick):
        desiredCard = self.cards.pop(pick)
        return desiredCard