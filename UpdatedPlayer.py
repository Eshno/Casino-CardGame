#from UpdatedDeck import Deck
from Middle import Middle

class Player:
    def __init__(self, name,cards, bank, points, tookLast):
        self.name = name
        self.cards = []
        self.bank = []
        self.points = 0
        self.tookLast = tookLast


    @property
    def show_points(self):
        return '{} points: {}'.format(self.name , self.points)

    @property
    def show_name(self):
        return '{}'.format(self.name)

    def bank_amt(self):
        return len(self.bank)

    def __len__(self):
        return len(self)

    def hasNocards(self):
        return len(self.cards) == 0

    def CleanBank(self):
        self.bank = []

    def Refill(self):
        return


    def show_Cards(self):
        print "Your Hand: \n"
        count = 1
        for i in self.cards:
            if i[0] == 1:
                print "((" + str(count) + "))",  "Ace of", i[1] , "|" ,
            else:
                print "((" + str(count) + "))",  i[0], "of", i[1] , "|" ,
            count +=1
