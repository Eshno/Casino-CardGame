#from UpdatedDeck import Deck
from UpdatedMiddle import Middle

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.bank = []
        self.points = 0
        self.tookLast = False

    @property
    def Show_Player_Points(self):
        return '{} points: {}'.format(self.name , self.points)

    @property
    def Show_Player_Name(self):
        return '{}'.format(self.name)

    def Bank_Cards_Amount(self):
        return len(self.bank)

    def Cards_Left(self):
        return len(self)

    def hasCards(self):
        return len(self.cards) == 0

    def Clean_Player_Bank(self):
        self.bank = []
    
    def Get_Card(self, card):        
        self.cards.append(card)
            

    def Show_Player_Cards(self):
        print "Your Hand: \n"
        count = 1
        for card in self.cards:
            if card[0] == 1:
                print "((" + str(count) + "))",  "Ace of", card[1] , "|" ,
            else:
                print "((" + str(count) + "))",  card[0], "of", card[1] , "|" ,
            count +=1
