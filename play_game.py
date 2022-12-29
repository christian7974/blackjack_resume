"""
Functions for gameplay are created here; this is the file where all of the gameplay will occur
"""
from start_game import Card, master_deck
def deal_card_from(deck: list[Card]) -> Card:
    return deck.pop()

top_card = deal_card_from(master_deck)
top_card.print_card()