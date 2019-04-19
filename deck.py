from random import randint
from card import Card

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