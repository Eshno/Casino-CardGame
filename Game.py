from UpdatedDeck import Deck
from Card import Card
from UpdatedPlayer import Player
from UpdatedMiddle import Middle



players = []
names = ["Roger", "Shanon", "Carlo", "Carlos"]


class Game:    
    players = []
    player_amount = input("Insert Player Amount [2-4]")
    def __init__(self):
        self.deck = Deck()
        self.deck.Create_Shuffle_Deck()
        self.middle = Middle() 
        Game.Create_Players()

    @classmethod
    def Create_Players(cls):
        names = ["Roger", "Shanon", "Carlo", "Carol"]
        for p in range(0, cls.player_amount):
            cls.players.append(Player(names[p]))
        
            
         
def Start_Up():
    for player in ThisGame.players:
        for i in range(0,4):
            player.Get_Card(ThisGame.deck.Deal_Card())
    for i in range(0,4):
        ThisGame.middle.Get_Card(ThisGame.deck.Deal_Card())
            


ThisGame = Game()
Start_Up()

# for i in range (0,len(ThisGame.players)):
#     print ThisGame.players[i].__dict__

print ThisGame.middle.__dict__

# for player in range(0,ThisGame.player_amount):
#     print ThisGame.players[player].__dict__

# print ThisGame.deck.cards
