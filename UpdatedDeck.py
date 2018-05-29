import random
from Cards import Card
from UpdatedPlayer import Player


class Deck:
    def __init__(self, cards = []):
        self.cards = []

    def Create_Deck(self):
        for type in Card.card_type:
            for card in Card.cards:
                self.cards.append([card, type])

    def Shuffle(self):
        to_shuffle = []
        for pos in range (0, len(self.cards)):
            picked = random.choice(self.cards)
            to_shuffle.append(picked)
            self.cards.remove(picked)
        self.cards = to_shuffle

    def Deal_Cards():  

        return
