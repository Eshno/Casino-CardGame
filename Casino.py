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
        players["player" + str(i)] = {"Cards": [], "Bank": [], "Points": 0}





#Deals cards to players and middle (only deals to middle...
#... if hasBegun is True)
def Deal(deck, amount,hasBegun):
    """Deals cards"""
    for i in range(1,amount + 1):     
        players["player"+str(i)]["Cards"] = Deal_Cards(players["player"+str(i)]["Cards"], deck)

    if hasBegun:
        Deal_Cards(middle["Main"], deck)
        hasBegun = False
    

def Play_Card(player_num,played_card):       
    
    select = input("Would you like to Pair the card or Claim it? [0(Pair) / 1(Claim)]")
    if select == 1:
        print "The Card: ", played_card
        for i in middle["Main"]:
            if played_card[0] == i[0]:
                players["player" + str(player_num)]["Bank"].append(i)
                players["player" + str(player_num)]["Bank"].append(played_card)
                middle["Main"].remove(i)
                return
                
        
        
 
   
         
    

def IsPairable():
    return

def IsCombinable():
    return

def IsPlayable(played_card):
    for i in middle["Main"]:
        if played_card[0] == i[0]:
            return True
    
    #If the card is in Paired as well.
    #If the card value is in Combined as well.
    #If you cannot play any card, then you must place any card from your deck.
    return False

def AnyPossiblePlay(player_num):
    for p in players["player" + str(player_num)]["Cards"]:
        for m in middle["Main"]:
            if p[0] == m[0]:
                return True
    return False

def Place_Card(played_card):
    middle["Main"].append(played_card)
    players["player1"]["Cards"].remove(played_card)


def Play():
    for i in range(1,amount + 1):
        if i == 1:
            print "\nMiddle Cards: ", middle["Main"]            
            print "Paired Cards: ", middle["Paired"]
            print "Combined Cards: ", middle["Combined"]
            print "\nYour Cards: ", players["player1"]["Cards"]
            if not AnyPossiblePlay(i):
                print "\n\nThere's no possible play, a card must be placed"
                print "Select a Card to place: [1 - " + str(len(players["player1"]["Cards"])) + "]"
                select = input("")  
                Place_Card(players["player1"]["Cards"][select - 1])

            else:

                print "Select a Card: [1 - " + str(len(players["player1"]["Cards"])) + "]"
                select = input("")            
                if select > 4 or select < 1 or not IsPlayable(players["player1"]["Cards"][select - 1]):
                    print "Please select a Valid Card"
                    Play()
                else:
                    if IsPlayable(players["player1"]["Cards"][select - 1]):
                        print "Played card: " , players["player1"]["Cards"][select - 1]
                        Play_Card(i , players["player1"]["Cards"][select - 1])
                        print "\nPlayer Bank: ",players["player1"]["Bank"], "Middle: ", middle["Main"]

    

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




    

    
