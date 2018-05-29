
class Card:
    cards = [1,2,3,4,5,6,7,8,9,10,"Jack", "Queen" ,"King"]
    card_type = ["Diamonds", "Spades", "Hearts", "Clubs"]
    card = 0
    type = 0


    def __init__(self):
        pass

    def Create_Card(cls):
        cls.card += 1
        if cls.card > 13:
            cls.card , cls.type = 0 , type + 1
        return cls.cards[cls.card - 1] , cls.card_type[cls.type]

    def Reset(cls):
        cls.card_num , cls.type_num = 0 , 0
