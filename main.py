import random

class Card:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def show(self):
        print self.type, self.number

class Deck:
    cards = []
    types = ['spades', 'diamonds', 'hearts', 'clubs']

    def generate(self):
        for type in Deck.types:
            for number in range(1, 14):
                newCard = Card(type, number)
                Deck.cards.append(newCard)
    
    def shuffle(self):
        shuffledDeck = []
        for i in range(0,53):
            shuffledCard = random.choice(Deck.cards)
            shuffledDeck.append(shuffledCard)
        Deck.cards = shuffledDeck
    
    def generateAndShuffle(self):
        self.generate()
        self.shuffle()
    
    def deal(self):
        dealedCard = Deck.cards.pop(0)
        return dealedCard
            
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
    
    def showCards(self):
        for card in self.cards:
            print card.type , card.number
    
    def receiveCard(self, card):
        self.cards.append(card)

class Error:
    errorMessage = ''
    def isPlayerAmountValid(self, amount):
        isValid = amount > 0 and amount <= 4 
        if not isValid: 
            Error.errorMessage = 'Player Amount is Not Valid'
        return isValid

def createPlayers(amount):
    if not errorHandle.isPlayerAmountValid(amount):
        print errorHandle.errorMessage
        return
    availablePlayerNames = ['Rose', 'Olive', 'Jorge', 'Maria']
    players = []
    for i in range(0, 4): 
        players.append(Player(availablePlayerNames[i]))
    return players


deck = Deck()
errorHandle = Error()
deck.generate()
playerAmount = 4
players = createPlayers(playerAmount)

for card in deck.cards:
    print card.__dict__
print len(deck.cards)