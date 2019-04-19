from random import randint

class Card:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def show(self):
        print self.type, self.number

class Deck:
    types = ['spades', 'diamonds', 'hearts', 'clubs']

    def __init__(self):
        self.cards = []

    def generate(self):
        for type in Deck.types:
            for number in range(1, 14):
                newCard = Card(type, number)
                self.cards.append(newCard)
    
    def shuffle(self):
        shuffledDeck = []
        for i in range(1,53):
            shuffledCard = self.cards.pop(randint(0, len(self.cards) -1))
            shuffledDeck.append(shuffledCard)
        self.cards = shuffledDeck
    
    def generateAndShuffle(self):
        self.generate()
        self.shuffle()
    
    def deal(self):
        dealedCard = self.cards.pop()
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

class Middle:

    def __init__(self):
        self.cards = []


class Error:
    errorMessage = ''
    def isPlayerAmountValid(self, amount):
        isValid = amount > 0 and amount <= 4 
        if not isValid: 
            Error.errorMessage = 'Player Amount is Not Valid'
        return isValid

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
    
    def prepareDeck(self):
        self.deck.generateAndShuffle()
    
    def preparePlayers(self):
        availablePlayerNames = ['Rose', 'Olive', 'Jorge', 'Maria']
        for i in range(0,4):
            self.players.append(Player(availablePlayerNames[i]))
    
    def startUpDeal(self):
        for player in self.players:
            for i in range(0,7):
                card = self.deck.deal()
                player.receiveCard(card)


# def createPlayers(amount):
#     if not errorHandle.isPlayerAmountValid(amount):
#         print errorHandle.errorMessage
#         return
#     availablePlayerNames = ['Rose', 'Olive', 'Jorge', 'Maria']
#     players = []
#     for i in range(0, 4): 
#         players.append(Player(availablePlayerNames[i]))
#     return players

errorHandle = Error()
game = Game()
game.prepareDeck()
game.preparePlayers()
game.startUpDeal()
# print game.deck.cards
# for card in game.deck.cards:
#     print card.__dict__
# for player in game.players:
#     print player.name
#     for card in player.cards:
#         print card.__dict__