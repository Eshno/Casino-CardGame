class Player:

    def __init__(self, name,cards, bank, points):
        self.name = name
        self.cards = []
        self.bank = []
        self.points = 0
        
    @property
    def show_points(self):
        return '{} - {}'.format (self.name , self.points)

    @property
    def show_cards(self):
        return 'Your Cards: {}'.format (self.cards)

    
    def bank_amt(self):
        return len(self.bank)

    def __len__(self):
        return len(self)

    @staticmethod
    def hasNocards(self):
        if len(self.cards) <= 0:
            return True
        return False
        
    
