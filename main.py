from random import randint
from player import Player
from deck import Deck
from middle import Middle
from card import Card

class Game:
    def __init__(self):
        self.deck = Deck()
        self.middle = Middle()
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
    
    def prepareMiddle(self):
        for i in range (0,4): 
            card = self.deck.deal()
            self.middle.receiveCard(card)

game = Game()
game.prepareDeck()
game.preparePlayers()
game.startUpDeal()
# print game.deck.cards
# for card in game.deck.cards:
#     print card.__dict__
for player in game.players:
    print player.name
    for card in player.cards:
        print card.__dict__