import random

#cards = ["Ace",2,3,4,5,6,7,8,9,10,"Jack", "Queen" ,"King"]
#card_type = ["Diamonds", "Spades", "Hearts", "Clubs"] 

main_deck = []

player1 = []
player2 = []
player3 = []
player4 = []    



class Deck:    
    cards = ["Ace",2,3,4,5,6,7,8,9,10,"Jack", "Queen" ,"King"]
    card_type = ["Diamonds", "Spades", "Hearts", "Clubs"]
    deck = []

    def __init__(self, deck):
        self.deck = deck
        
        
    
    @classmethod
    def Create_Deck(cls, deck):
        """Generates an ordered deck"""
        print "Generating Deck..."        
        for ct in cls.card_type:    
            for c in cls.cards:
                deck.append([c,ct])
        print "Deck Generated."        
        return deck

       
    def Shuffle_Deck(self, deck):
        """Shuffes the Deck"""
        to_shuffle = []
        picked = None
        print "Shuffling Deck..."
        for i in range(0, len(deck)):
            picked = random.choice(deck)
            to_shuffle.append(picked)
            deck.remove(picked)        
        deck = to_shuffle
        print "Deck Shuffled."
        return deck

    def __len__(self):
        return len(self)
            
        


#Deck.Create_Deck(main_deck)
#main_deck = 

#print main_deck, "\n" , len(main_deck)

        
class Deal():
    def __init__(self):
        pass



"""
def Make_Deck(deck):
    
    for ct in card_type:    
        for c in cards:
            deck.append([c,ct])
    return deck
    

def Shuffle_Deck(deck):
    
    to_shuffle = []
    picked = None
    for i in range(0,len(deck)):
        picked = random.choice(deck)
        to_shuffle.append(picked)
        deck.remove(picked)
    deck = []
    #print to_shuffle ,"\n", len(to_shuffle)
    return to_shuffle
        




def Deal_Cards(player,deck):
    
    for i in range(0,4,1):        
        player.append(deck[i])
    for i in player:
        deck.remove(i)
    return player

"""

#Make_Deck(main_deck)
#main_deck = Shuffle_Deck(main_deck)

"""
player1 = Deal_Cards(player1, main_deck)
player2 = Deal_Cards(player2, main_deck)
player3 = Deal_Cards(player3, main_deck)
player4 = Deal_Cards(player4, main_deck)


print "player 1: "
print player1
print "player 2: "
print player2
print "player 3: "
print player3
print "player 4: "
print player4
"""
#print "\nDeck: " , main_deck, "\n", len(main_deck)

   
