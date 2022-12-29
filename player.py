"""
player.py file where the player class is initialized and all of the methods for the player will be created
"""
from start_game import Card
""""""
class Player:
    """
    The player that will be participating in the game.
    Field:
        hand (list[Card]): the cards that are in the player's hand for a round
        has_bust (bool): indicates if the player has gone over 21
        score (int): the score of the player for the round
        next_move (str): what the player's next move will be (hit, stand, double down, etc)
    """
    def __init__(self):
        self.hand: list[Card] = []
        self.has_bust = False
        self.score = 0
        self.next_move = ""