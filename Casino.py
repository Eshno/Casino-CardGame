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

def Place_Card(played_card, player_num):
    middle["Main"].append(played_card)
    players["player" + str(player_num)]["Cards"].remove(played_card)


def Claim_Card(played_card, claimed_card, player_num):    
    if played_card[0] == claimed_card[0]:
        players["player" + str(player_num)]["Bank"].append(played_card)
        players["player" + str(player_num)]["Bank"].append(claimed_card)
        players["player" + str(player_num)]["Cards"].remove(played_card)
        middle["Main"].remove(claimed_card)
        return
    print "\n\nNot a valid Claim\n"
    Play()
            
def Pair_Card():
    return
    


def Play():
    for i in range(1,amount + 1):
        if i == 1:
            print "\nMiddle Cards: ", middle["Main"]            
            print "\nPaired Cards: ", middle["Paired"]
            print "\nCombined Cards: ", middle["Combined"]
            print "\n\nYour Cards: ", players["player1"]["Cards"]       
            

            print "Select a Card: [1 - " + str(len(players["player1"]["Cards"])) + "]"
            select = input("")            
            if select > 4 or select < 1:
                print "\nSelect a valid card\n"
                Play()
            else:
                print "Selected Card: ", players["player" + str(i)]["Cards"][select - 1]
                move = input ("Would you like to Place(1) ,Claim(2), Pair(3), Combine(4) or Select another card(0)?")
                if move == 0:
                    Play()
                if move == 1:
                    Place_Card(players["player" + str(i)]["Cards"][select - 1], i) #Card / Player Works!
                    Play() #TesT!
                if move == 2:
                    print "\n\nMiddle Cards: ", middle["Main"]
                    print "Select the Card from the middle you'd like to claim: [1 - " + str(len(middle["Main"])) + "]"
                    m_select = input ("")
                    Claim_Card(players["player" + str(i)]["Cards"][select - 1] , middle["Main"][m_select - 1], i)
                    print "My Bank: " , players["player1"]["Bank"]
                    Play()
                if move == 3:
                    return #Pair
                if move == 4:
                    return #Combine
                
        #The rest of the players turn

    

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




    

    
