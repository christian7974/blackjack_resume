"""
File where the game is started (deck, player, dealer are initialized)
"""
import random
from player import Player
from dealer import Dealer
class Card:
    """
    An individual card that will be used in the game
    Field:
        worth (int): how much the card is worth (2-11)
        suit (str): the suit of the card (diamonds, heart, etc)
        on_card (str): what it says on the card (2, ace, queen, etc.)
    """
    def __init__(self, worth, suit, on_card):
        self.worth = worth
        self.suit = suit
        self.on_card = on_card

    def print_card(self):
        print("a", self.on_card, "of", self.suit)

def initialize_deck():
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
                worth_amount = 11
            elif j == 11:
                val_on_card = "Jack"
                worth_amount = 10
            elif j == 12:
                val_on_card = "Queen"
                worth_amount = 10
            elif j == 13:
                val_on_card = "King"
                worth_amount = 10
            else:
                val_on_card = j
                worth_amount = j
            single_card = Card(worth_amount, suit_of_card, val_on_card)
            deck.append(single_card)
    random.shuffle(deck)   
    return deck
master_deck = initialize_deck()
player_1 = Player()
the_dealer = Dealer()