import random

class Card:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def show(self):
        return self.type, self.number


class Deck:
    cards = []
    types = ['spades', 'diamonds', 'hearts', 'clubs']

    def generate(self):
        for type in Deck.types:
            for num in range(1, 14):
                newCard = Card(type, num)
                Deck.cards.append(newCard)
    
    def shuffle(self):
        shuffledDeck = []
        for i in range(0,53):
            shuffledCard = random.choice(Deck.cards)
            shuffledDeck.append(shuffledCard)
        Deck.cards = shuffledDeck
            


deck = Deck()
deck.generate()

# print random.choice(deck.cards).__dict__

# print len(deck.cards)

print deck.shuffle()
for card in deck.cards:
    print card.type, card.number
