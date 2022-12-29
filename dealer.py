"""
dealer.py file where the dealer class is initialized and all of the methods for the dealer will be created
"""
class Dealer:
    def __init__(self):
        from start_game import Card
        self.hand: list[Card] = []
        self.has_bust = False
        self.blackjack = False
        self.score = 0
        self.next_move = ""