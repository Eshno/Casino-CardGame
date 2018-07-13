# Casino-CardGame

Using random.py from the cpython Library.
https://github.com/python/cpython

***Ignorar los archivos que llevan Updated...***

Game.py es el principal.

Deck.py genera las cartas.

Middle.py es donde se colocan las cartas.

Player.py es el jugador.

***Working on Updates***

How to Play:

You first start off by introducing the players amount (2 to 4).

After the amount of players is introduced, you'll immediatly start to play.

In every turn, you must choose the current player card from his hand depending on what's 
in the middle, then you must choose what do you want to do with that card.

You have the next options:
Place the Card -
Claim a Card - 
Pair the Card -
Combine the Card -
Select another Card.

Everytime a player runs out of Cards, its cards will be refilled as long as there are
cards remaining in the main deck (at the moment there's nothing being showed to keep 
track of how many cards are remaining).

When all the players run out of cards and there are no more cards in the main deck, then the player
who claimed last will automatically claim the cards left in the middle.

After this, the Score is going to be set and showed. Then, you may decide to continue playing or to end
the game right away.

If you choose to continue playing, the deck will be created again, shuffled and dealed to every player and the middle.
Players won't keep the cards that they claimed in the last game.
Players will keep their Score from the previous game.
