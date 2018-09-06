import random



class Deck:    
    cards = [1,2,3,4,5,6,7,8,9,10,"Jack", "Queen" ,"King"]
    card_type = ["Diamonds", "Spades", "Hearts", "Clubs"]
    deck = []

    def __init__(self, deck):
        self.deck = deck
    
    @classmethod
    def Create_Deck(cls, deck):
        """Generates a Deck"""        
        for ct in cls.card_type:    
            for c in cls.cards:
                deck.append([c,ct])        
        cls.deck = deck
        return deck
    
    @classmethod
    def Shuffle_Deck(cls, deck):
        to_shuffle = []
        for i in range(0, len(cls.deck)):
            picked = random.choice(deck)
            to_shuffle.append(picked)
            cls.deck.remove(picked)
        cls.deck = to_shuffle
        return to_shuffle

    @classmethod
    def deal_card(cls, obj):        
        return cls.deck.pop(0)
    
        
        

