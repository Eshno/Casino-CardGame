import random

cards = ["Ace",2,3,4,5,6,7,8,9,10,"Jack", "Queen" ,"King"]
card_type = ["Diamonds", "Spades", "Hearts", "Clubs"]
deck = []

players = {}
middle = {"Main": [], "Paired": [],"Combined": []}
hasBegun = True

amount = input("Ingrese cantidad de Jugadores: ")



# Deck Creator
def Create_Deck(deck):
    """Creates an unshuffled deck"""
    print "Creating deck..."
    deck = []
    for ct in card_type:    
        for c in cards:
            deck.append([c,ct])
    print "Deck Created."
    return deck
    




#Deck Shuffler
def Shuffle_Deck(deck):
    """Shuffles the deck"""    
    to_shuffle = []
    picked = None
    print "Shuffling deck..."
    for i in range(0,len(deck)):
        picked = random.choice(deck)
        to_shuffle.append(picked)
        deck.remove(picked)    
    print "Deck Shuffled."
    return to_shuffle


# Card Dealing
def Deal_Cards(player,deck):
    """Deals 4 cards"""    
    for i in range(0,4):        
        player.append(deck[i])
    for i in player:
        deck.remove(i)
    return player





# Create Players
def Create_Players(deck, amount):
    for i in range(1,amount + 1):        
        players["player" + str(i)] = {"Cards": [], "Bank": []}





#Deals cards to players and middle (only deals to middle...
#... if hasBegun is True)
def Deal(deck, amount,hasBegun):
    """Deals cards"""
    for i in range(1,amount + 1):     
        players["player"+str(i)]["Cards"] = Deal_Cards(players["player"+str(i)]["Cards"], deck)

    if hasBegun:
        Deal_Cards(middle["Main"], deck)
        hasBegun = False
    

def Play_Card():    
    return

def IsPairable():
    return

def IsCombinable():
    return

def IsPlayable(played_card):
    for i in middle["Main"]:
        if played_card[0] == i[0]:
            return True 
    return False

def Play():
    for i in range(1,amount + 1):
        if i == 1:
            print "\nMiddle Cards: ", middle["Main"]            
            print "Paired Cards: ", middle["Paired"]
            print "Combined Cards: ", middle["Combined"]
            print "\nYour Cards: ", players["player1"]["Cards"]            
            print "Seleccione su carta: [1 - " + str(len(players["player1"]["Cards"])) + "]"
            select = input("")            
            if select > 4 or select < 1 or not IsPlayable(players["player1"]["Cards"][select - 1]):
                print "Seleccione una carta valida"
                Play()
            else:
                if IsPlayable(players["player1"]["Cards"][select - 1]):
                    print "Played card: " , players["player1"]["Cards"][select - 1]
                    #Play_Card(players["player1"]["Cards"][select - 1])
                
    

deck = Create_Deck(deck)
deck = Shuffle_Deck(deck)
#print "Actual Deck" , deck, len(deck)
Create_Players(deck, amount)
Deal(deck,amount,hasBegun)
Play()

"""
for i in range (1,len(players) + 1):
    print "player"+str(i)
    print players["player"+str(i)]"""
#print "Middle: ", middle["Main"], len(deck)

#print deck, "\n" ,len(deck)




    

    
