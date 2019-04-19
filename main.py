from random import randint
from card import Card
from deck import Deck
from error import Error
from middle import Middle
from player import Player

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
    
    def startUpDealToPlayers(self):
        for player in self.players:
            for i in range(0,7):
                card = self.deck.deal()
                player.receiveCard(card)
    
    def prepareMiddleCards(self):
        for i in range (0,4): 
            card = self.deck.deal()
            self.middle.receiveCard(card)

game = Game()
game.prepareDeck()
game.preparePlayers()
game.startUpDealToPlayers()
game.prepareMiddleCards()

# for card in game.middle.cards:
#     print card.__dict__
# print game.deck.cards
# for card in game.deck.cards:
#     print card.__dict__
# print len(game.deck.cards)
# for player in game.players:
#     print player.name
#     for card in player.cards:
#         print card.__dict__