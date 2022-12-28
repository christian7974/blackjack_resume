"""
File where the game is started (deck, player, dealer are initialized)
"""
from player import *

class Card:
    def __init__(self, worth, suit, on_card):
        self.worth = worth
        self.suit = suit
        self.on_card = on_card

def initialize_deck():
    num_cards = 0
    deck: list[Card] = []
    for i in range(0, 4): # loop thru 4 suits
        if i == 0:
            suit_of_card = "hearts"

        elif i == 1:
            suit_of_card = "diamonds"

        elif i == 2:
            suit_of_card = "spades"

        elif i == 3:
            suit_of_card = "clubs"

        for j in range(1, 14): # loop thru 13 values
            if j == 1:
                val_on_card = "Ace"

            elif j == 11:
                val_on_card = "Jack"

            elif j == 12:
                val_on_card = "Queen"

            elif j == 13:
                val_on_card = "King"
            else:
                val_on_card = j
            single_card = Card(j, suit_of_card, val_on_card)
            deck.append(single_card)
    for card in deck:
        print("this is a", card.on_card, "of", card.suit)
    print(len(deck))
initialize_deck()