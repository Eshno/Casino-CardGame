import random


cards = ["Ace",2,3,4,5,6,7,8,9,10,"Jack", "Queen" ,"King"]
card_type = ["Diamonds", "Spades", "Hearts", "Clubs"]
deck = []

players = {}
middle = {"Main": [], "Paired": [],"Combined": []}
hasBegun = True

amount = input("Insert the players amount: [2 - 4] ")
ValidMove = False


#Deck Creator
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
        return True
    else:
        print "\n\nNot a valid Claim\n"        
        return False


            
def Pair_Card(played_card, toPair_card, player_num):    
    if played_card[0] == toPair_card[0]:
        players["player" + str(player_num)]["Cards"].remove(played_card)
        middle["Paired"].append(played_card)
        middle["Paired"].append(toPair_card)
        middle["Main"].remove(toPair_card)        
        return True
    else:        
        print "These cards are not pairable"
        return False
        
    
def Pair_Claim_Avaiable():
    if len(middle["Paired"]) > 0:
        return True
    return False

def Combine_Claim_Avaiable():
    if len(middle["Combined"]) > 0:
        return True
    return False

def Claim_Pair_Card():
    return

def Is_Over(deck_cards , left_cards):
    if left_cards == 0 and deck_cards == 0:
        #Remember that if you want to restart the game, hasBegun must be True again.
        return True
    else:
        return False
    
def Score():
    points = 0
    for i in players:
        if [10, "Diamonds"] in players[i]["Cards"]:# If has 10 of Diamonds 2+ (Big Casino)
            players[i]["Points"] += 2
        if [2, "Spades"] in players[i]["Cards"]:# If has 2 of Spades 1+ (Little Casino)
            players[i]["Points"] += 1
        for c in players[i]["Cards"]:# For each ace 1+
            if c[0] == "Ace":
                players[i]["Points"] += 1
        if Most_Cards(len(players[i]["Cards"])):
            points += 3
        if Most_Spades():
            points += 1    
    return

def Most_Cards(card_amount):
    most = 0
    if amount == 2:
        most = max(len(players["player1"]["Cards"], players["player2"]["Cards"]))
    if amount == 3:
        most = max(len(players["player1"]["Cards"], players["player2"]["Cards"], players["player3"]["Cards"]))
    if amount == 4:
        most = max(len(players["player1"["Cards"]], players["player2"]["Cards"], players["player3"]["Cards"], players["player4"]["Cards"]))
    for p in players:
        if card_amount == most_cards:
            return True
    return False

def Most_Spades():
    spade_count = [None]
    for i in players:
        spade_count.append(0)
        for c in players[i]["Cards"]:
            if c[1] == "Spades":
                spade_count[int(i[-1])] += 1 # int(i[-1]) = players->[1]<- as an int
    most_spades = max(spade_count)
    for p in players:
        if spade_count[int(p[-1])] == most_spades:
            return True
    return False

def Play():
    for i in range(1,amount + 1):
        while True:
            
            print "\n\n-----------Player " + str(i) + " turn-----------\n\n"
            print "\nMiddle Cards: ", middle["Main"]            
            print "\nPaired Cards: ", middle["Paired"]
            print "\nCombined Cards: ", middle["Combined"]
            print "\n\nYour Cards: ", players["player" + str(i)]["Cards"]       
                

            print "Select a Card: [1 - " + str(len(players["player" + str(i)]["Cards"])) + "]"
            select = input("")            
            if select > 4 or select < 1:
                print "\nSelect a valid card\n"
                #Play()
            else:
                print "Selected Card: ", players["player" + str(i)]["Cards"][select - 1]
                move = input ("Would you like to Place(1) ,Claim(2), Pair(3), Combine(4) or Select another card(0)?")
                if move == 0:# Select another card
                    continue

                
                if move == 1:#Place a card
                    Place_Card(players["player" + str(i)]["Cards"][select - 1], i) #Card / Player Works!
                    break

                
                if move == 2: #Claim
                    ValidMove = False
                    print "\n\nMiddle Cards: ", middle["Main"]
                    print "\nPaired Cards: ", middle["Paired"]
                    print "\nCombined Cards: ", middle["Combined"]                    
                    #if Pair_Claim_Avaiable or Combined_Claim_Avaiable: Always ask this (commented section)
                     #   c_select = input ("What kind of claim would you like to do?:-> Normal Claim (1), Paired Claim(2), Combined Claim(3)")
                      #  if c_select == 1:
                            #All from below
                    
                            
                    print "Select the Card from the middle you'd like to claim: [1 - " + str(len(middle["Main"])) + "]"
                    m_select = input ("")
                    ValidMove = Claim_Card(players["player" + str(i)]["Cards"][select - 1] , middle["Main"][m_select - 1], i)
                    #print "My Bank: " , players["player1"]["Bank"]
                    #print ValidMove
                    if not ValidMove:
                        continue
                    break

                
                if move == 3: #Pair
                    ValidMove = False
                    print "\n\nMiddle Cards: ", middle["Main"]
                    print "Select the Card from the middle you'd like to pair: [1 - " + str(len(middle["Main"])) + "]"
                    m_select = input("")
                    ValidMove = Pair_Card(players["player" + str(i)]["Cards"][select - 1], middle["Main"][m_select - 1], i)
                    if not ValidMove:
                        continue
                    break

                
                if move == 4:#Combine
                    print "This ain't finished"
                    continue    

    if len(players["player" + str(amount)]["Cards"]) == 0 and len(deck) > 0: #Refill Cards
        Deal(deck,amount,hasBegun)
        
    if Is_Over(len(deck), len(players["player1"]["Cards"])):
        print "Game Over..."
        #Score()
        return
    Play()

    

deck = Create_Deck(deck)
deck = Shuffle_Deck(deck)
#print "Actual Deck" , deck, len(deck)
Create_Players(deck, amount)
hasBegun = Deal(deck,amount,hasBegun)
Play()

"""
for i in range (1,len(players) + 1):
    print "player"+str(i)
    print players["player"+str(i)]"""
#print "Middle: ", middle["Main"], len(deck)

#print deck, "\n" ,len(deck)




    

    
