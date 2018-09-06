from Player import Player
from Deck import Deck
from Middle import Middle

players = {} # Used to access the player object.
amount = 0 # Used to Determine the amount of player.
someobj = [] 
ValidMove = False # Determines if a move is Valid.

""" ---------------------------- Start ----------------------------"""

def Create_Players():
    #This function is used to create the players 
    while True:# This loop is to prevent that an unwished amount is inputted.
        amount = input ("Insert player amount [2-4]") #Determines the amount of players
        if amount >= 2 and amount <= 4:
            break
    #Instanciation of the player object.
    players["player1"] = Player("Roger" , [] , [], 0, False)
    players["player2"] = Player("Shanon" , [] , [], 0, False)
    if amount >= 3:
        players["player3"] = Player("Carol" , [] , [],0, False)
    if amount == 4:
        players["player4"] = Player("Carlo" , [] , [], 0, False)
    return amount
        

def StartUp():#Used  to Start the Game
    #Clears the Deck, creates it (fill it w/ cards) and shuffles it.
    Deck.deck = []
    Deck.Create_Deck(someobj)
    Deck.Shuffle_Deck(someobj)  
    #Deals the cards one by one to the players and the middle
    for i in range(0,4):
        Middle.cards.append(Deck.deal_card(someobj))
        for p in range(1,amount + 1):
            players["player" + str(p)].cards.append(Deck.deal_card(someobj))
        
    print "\n\nNew Game Started\n\n"    
    Play()#Start
    return







""" ---------------------------- Card Managing ----------------------------"""

def Place_Card(selected_card, turn):
    #As the function name mentions, places a card, removing it from the player hand and appending it to the middle.
    Middle.cards.append(selected_card)
    players["player" + str(turn)].cards.remove(selected_card)
    print "\n\n",players["player" + str (turn)].show_name, "has placed a card\n\n"
    return
    
def Claim_Card(selected_card, turn):
    #This function appends the selected card(s) from the middle and the selected card from your hand to the player bank
    #only if the conditions are met.
    Middle.show_middle()
    if selected_card[0] == 1:
        print "Your Card: " , "Ace of", selected_card[1] , "\n"
    else:
        print "Your Card: " , selected_card[0], "of", selected_card[1] , "\n"
    toClaim = input("Select the Card(s) you'd like to claim: ")
    
    if toClaim > len(Middle.cards) or toClaim <= 0:#If the toClaim value is not valid, then it will reset the current turn.
        return False
    if selected_card[0] == Middle.cards[toClaim - 1][0]:
        #If the card values are the same, then it will proceed to append to the bank and remove from the middle.
        if Middle.cards[toClaim - 1][-1] == "Paired" or Middle.cards[toClaim - 1][-1] == "Combined":
            #In case that the selected card is paired or combined, this method will execute.
            for i in range (1, len(Middle.cards[toClaim - 1]) - 1):                
                players["player" + str(turn)].bank.append(Middle.cards[toClaim - 1][i])                
            players["player" + str(turn)].bank.append(selected_card)
            Middle.cards.remove(Middle.cards[toClaim - 1])
            players["player" + str(turn)].cards.remove(selected_card)
            print "\n\n",players["player" + str (turn)].show_name, "has Claimed a card\n\n"
            return True
        else:
            #In case the selected card from the middle is single, then the card selected from your hand and the middle
            #will be appended to the current player bank, the selected cards will also be removed from the middle/your hand.
            players["player" + str(turn)].bank.append(Middle.cards[toClaim - 1])
            players["player" + str(turn)].bank.append(selected_card)
            Middle.cards.remove(Middle.cards[toClaim - 1])
            players["player" + str(turn)].cards.remove(selected_card)
            print "\n\n",players["player" + str (turn)].show_name, "has Claimed a card\n\n"
            return True
    return False

def NewClaim(selected_card, turn):# This is a new way of Claiming (like auto-claiming and multi-claiming)
    toClaim = []
    #Checks if the sum of any cards is equal to the selected card, if so the cards will be added in toClaim
    for card1 in range (0, len(Middle.cards) - 2):
        if Middle.cards[card1][-1] in ["Paired", "Combined"] or Middle.cards[card1][0] in ["King", "Queen", "Jack"]:
            continue
        for card2 in range(card1 + 1, len(Middle.cards) - 1):
            if Middle.cards[card2][-1] in ["Paired", "Combined"] or Middle.cards[card2][0] in ["King", "Queen", "Jack"]:
                continue
            if Middle.cards[card1][0] + Middle.cards[card2][0] == selected_card[0]:
                if Middle.cards[card1] not in toClaim:
                    toClaim.append(Middle.cards[card1])
                if card2 not in toClaim:
                    toClaim.append(Middle.cards[card2])
                    
    #Checks if the value of a Card is equal to the selected card, if so the card will be added in toClaim
    #Also checks if there's a combination or pairing of cards.
    for card in Middle.cards:
        if card[0] == selected_card[0] and card not in toClaim:
            if card[-1] in ["Paired", "Combined"]:
                toClaim.append(card)
                for i in range (1, len(card) -1):
                    toClaim.append(card[i])
                continue
            toClaim.append(card)                 
    #Starts to add the cards to the player bank and removing them from the middle
    if len(toClaim) == 0:
        return False 
    for card in toClaim:               
        if card[-1] in ["Paired", "Combined"]:
            Middle.cards.remove(card)
            continue
        players["player" + str(turn)].bank.append(card)
        Middle.cards.remove(card)
    players["player" + str(turn)].bank.append(selected_card)
    players["player" + str(turn)].cards.remove(selected_card)
    players["player" + str(turn)].name , ":" ,players["player" + str(turn)].bank
    print "\n", players["player" + str(turn)].name , "has claimed.\n"
    return True

def Pair_Card(selected_card, turn):
    #Pairs the selected card from your hand with the card you select from the middle.
    Middle.show_middle()
    if selected_card[0] == 1:
        print "Your Card: " , "Ace of", selected_card[1] , "\n"
    else:
        print "Your Card: " , selected_card[0], "of", selected_card[1] , "\n"
        
    toPair = input("Select a card from middle you'd like to pair, \n Input an out of range num to reset your turn")
    if toPair <= 0 or toPair > len(Middle.cards):        
        return False
    
    if selected_card[0] == Middle.cards[toPair - 1][0]:
        #If the selected card from the middle is already paired, then this method will be executed.
        if Middle.cards[toPair - 1][-1] == "Paired":
            Middle.cards[toPair - 1].remove("Paired")
            Middle.cards[toPair - 1].append(selected_card)
            Middle.cards[toPair - 1].append("Paired")
            players["player" + str (turn)].cards.remove(selected_card)
            print "\n\n",players["player" + str (turn)].show_name, "has Paired a card\n\n"
            return True
        else:
            #In case the selected card from the middle is single, this method will be executed
            Middle.cards.append([])        
            Middle.cards[-1].append(selected_card[0])
            Middle.cards[-1].append(Middle.cards[toPair - 1])
            Middle.cards[-1].append(selected_card)
            Middle.cards[-1].append("Paired")
            players["player" + str (turn)].cards.remove(selected_card)
            Middle.cards.remove(Middle.cards[toPair - 1])
            print "\n\n",players["player" + str (turn)].show_name, "has Paired a card\n\n"
            return True
    return False



def Combine_Card(selected_card, turn):
    #Sums the values of the selected card from your deck and the selected card from the middle.
    #This sum cannot be bigger than 10
    if selected_card[0] in ["King", "Queen", "Jack"]:
        print "King, Queen or Jack cannot be Combined"
        return False
    
    Middle.show_middle()    
    if selected_card[0] == 1:
        print "Your Card: " , "Ace of", selected_card[1] , "\n"
    else:
        print "Your Card: " , selected_card[0], "of", selected_card[1] , "\n"
    toComb = input("Select a card from middle you'd like to Combine, \n Input an out of range num to reset your turn")
    if toComb <= 0 or toComb > len(Middle.cards):        
        return False
    
    if Middle.cards[toComb - 1][0] in ["King", "Queen", "Jack"]:
        print "\nKing, Queen or Jack cannot be Combined"
        return False
    
    if selected_card[0] + Middle.cards[toComb - 1][0] <= 10:      
        #In case the selected card from the middle is already combined.
        if Middle.cards[toComb - 1][-1] == "Combined":
            Middle.cards[toComb - 1].remove("Combined")
            Middle.cards[toComb - 1][0] += selected_card[0]
            Middle.cards[toComb - 1].append(selected_card)
            Middle.cards[toComb - 1].append("Combined")
            players["player" + str (turn)].cards.remove(selected_card)
            print "\n\n",players["player" + str (turn)].show_name, "has Combined a card\n\n"
            return True
        
        else:
            #In case the selected card from the middle is single.
            Middle.cards.append([])
            Middle.cards[-1].append(selected_card[0] + Middle.cards[toComb - 1][0])#The sum of both cards
            Middle.cards[-1].append(Middle.cards[toComb - 1])
            Middle.cards[-1].append(selected_card)
            Middle.cards[-1].append("Combined")
            players["player" + str (turn)].cards.remove(selected_card)
            Middle.cards.remove(Middle.cards[toComb - 1])
            print "\n\n",players["player" + str (turn)].show_name, "has Combined a card\n\n"
            return True            
    return False
    

def Refill(turn):
    #Whenever the player runs out of cards, its hand will be refilled with 4 cards.
    #This function will work until the main deck has no remaining cards.
    if len(Deck.deck) > 0:
        for i in range(0,4):
            players["player" + str(turn)].cards.append(Deck.deal_card(someobj))
    return








""" ---------------------------- End Game ----------------------------"""

def isOver():#Determines if the game is over by checking if the players and the main deck have no more cards left.
    if len(players["player1"].cards) == 0 and len(Deck.deck) == 0:        
        TakeRemaining()
        return True
    return False

def LastTake(turn):
    #Whenever a player claims, his tookLast atribute will be set True, the other players tookLast's value will be set to False.
    for p in range (1, amount + 1):        
        if p == turn:            
            players["player" + str(turn)].tookLast = True     
            continue
        players["player" + str(turn)].tookLast = False
    return

def TakeRemaining():
    #Looks for the player that has the tookLast in True, this player will have the remaining middle cards appended to its bank.
    for i in range(1, amount + 1):
        if players["player" + str(i)].tookLast:
            print players["player" + str(i)].name  ,"has taken the remaining cards\n"
            for mc in Middle.cards:# mc stands for middle card
                if mc[-1] == "Paired" or mc[-1] == "Combined":
                    for i in range(1, len(mc) - 1):
                        players["player" + str(i)].bank.append(mc[i])
                else:
                    players["player" + str(i)].bank.append(mc)
    Middle.cards = []    
    return

def bank_Cleanup():#Clears every player bank.
    for i in range(0, amount + 1):
        players["player"+ str(i)].CleanBank()
    return














""" ---------------------------- Score ----------------------------"""        
def Most_Cards(card_amount):
    most = 0
    #Determines the player with most cards in the bank depending on the amount of players playing currently.
    if amount == 2:#If there are 2 players
        most = max(len(players["player1"].bank), len(players["player2"].bank))
    if amount == 3:#If there are 3 players
        most = max(len(players["player1"].bank), len(players["player2"].bank), len(players["player3"].bank))
    if amount == 4:#If there are 4 players
        most = max(len(players["player1"].bank), len(players["player2"].bank), len(players["player3"].bank), len(players["player4"].bank))
    for i in range(1, amount + 1):
        if card_amount == most:
            return True
    return False

def Most_Spades(player):
    #Looks the player with most Spades in their bank.
    spade_count = [None]
    for i in range(1, amount + 1):
        spade_count.append(0)
        for c in players["player" + str(i)].bank:
            if c[1] == "Spades":
                spade_count[i] += 1
    most_spades = max(spade_count)
    for p in range(1, len(spade_count) - 1):
        if spade_count[p] == most_spades and p == player:
            return True
    return False   

def Score():
    #Sets the Score
    points = 0
    for i in range(1, amount + 1):# i indicates the player number
        if [10, "Diamonds"] in players["player" + str(i)].bank:#Big Casino
            points += 2
            #print "Big Casino: (+2)" , players["player" + str(i)].name
        if [2, "Spades"] in players["player" + str(i)].bank:# Little casino
            points += 1
            #print "Little Casino (+1): " , players["player" + str(i)].name
        for c in players["player" + str(i)].bank:# For each ace 1+
            if c[0] == 1:
                points += 1
                #print "Each Ace: (+1)" , players["player" + str(i)].name
        if Most_Cards(players["player" + str(i)].bank_amt):# Player with most cards
            points += 3
            #print "Most Cards: (+3)" , players["player" + str(i)].name
        if Most_Spades(i): # Player with most spades
            points += 1
            #print "Most Spades: (+1)" , players["player" + str(i)].name
        players["player" + str(i)].points += points
        points = 0    
    return

def show_Score():# Shows the score
    for i in range(1 , amount + 1):
        print players["player" + str(i)].show_points
    return











""" ---------------------------- Playing ----------------------------"""

def Play(): #Playing Function
    #Deck.deck = [] #Test
    for turn in range(1, amount + 1):
        while True:            
            print "\n\n" ,"-" * 5 + players["player" + str(turn)].show_name + "'s Turn" + "-" * 5, "\n\n"
            Middle.show_middle()
            print "\n\nSelect a Card from your Hand"
            players["player" + str(turn)].show_Cards()
            card_select = input("")
            if card_select > len(players["player" + str(turn)].cards) or card_select <= 0:
                continue
            selected_card = players["player" + str(turn)].cards[card_select - 1]
            if selected_card[0] == 1:
                print "Your Card: " , "Ace of", selected_card[1] , "\n"
            else:
                print "Your Card: " , selected_card[0], "of", selected_card[1] , "\n"            
            opt_select = input("What would you like to do?\nPlace Card [1] - Claim Card [2] - Pair Card [3] - Combine Card [4] - Select another Card [0]")            
            if opt_select > 4 or opt_select < 0:
                print "\n\nInvalid Option, try again\n"
                continue
            
            if opt_select == 1:#Place a Card
                Place_Card(selected_card, turn)                         
                break
            
            if opt_select == 2:#Claim a Card
                ValidMove = Claim_Card(selected_card, turn)
                #ValidMove = NewClaim(selected_card, turn)
                if not ValidMove:
                    print "\n\nNot a Valid Move, try again.\n"
                    continue                
                print "Bank: ", players["player" + str(turn)].bank #Test
                LastTake(turn)                
                break
            
            if opt_select == 3:#Pair a Card
                ValidMove = Pair_Card(selected_card, turn)
                if not ValidMove:
                    print "\n\nNot a Valid Move, try again.\n"
                    continue                
                break
            
            if opt_select == 4:#Combine a Card                
                ValidMove = Combine_Card(selected_card, turn)
                if not ValidMove:
                    print "\n\nNot a Valid Move, try again.\n"
                    continue                
                break
            
            if opt_select <= 0 or opt_select > 4:
                continue
            
        if len(players["player" + str(turn)].cards) == 0 and len(Deck.deck) != 0:#Refill cards
            Refill(turn)
            

    if not isOver():# Determines if the game is over
        Play()

    else: # If the game is over
        print "\n\nRound Over\n\n"
        Score()
        show_Score()
        newGame = None        
        while newGame != "1" or newGame != "2":# Ask to Start a new Game or end
            newGame = raw_input("\nWould you like to start a new game? Yes (1) / No(2)")
            if newGame == "1":
                bank_Cleanup()
                StartUp()
            elif newGame == "2":
                print "\n Thanks for playing"
                return        
            
    return

amount = Create_Players()
StartUp()







