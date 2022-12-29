"""
player.py file where the player class is initialized and all of the methods for the player will be created
"""

class Player:
    """
    The player that will be participating in the game.
    Field:
        hand (list[Card]): the cards that are in the player's hand for a round
        has_bust (bool): indicates if the player has gone over 21
        score (int): the score of the player for the round
    """
    def __init__(self):
        from start_game import Card
        self.hand: list[Card] = []
        self.second_hand: list[Card] = []
        self.has_bust = False
        self.blackjack = False
        self.score = 0