"""
dealer.py file where the dealer class is initialized and all of the methods for the dealer will be created
"""
class Dealer:
    def __init__(self):
        self.hand = []
        self.has_bust = False
        self.score = 0
        self.next_move = ""