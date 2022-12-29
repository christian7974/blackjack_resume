"""
Functions for gameplay are created here; this is the file where all of the gameplay will occur
"""
from start_game import Card, player_1, master_deck, the_dealer
from player import Player
from dealer import Dealer
from helpers import ask_input
user_options_first_turn = ['sp', 'split', 'h', 'hit', 's', 'stand', 'd', 'double']
user_options_subsequent_turn = ['h', 'hit', 's', 'stand', 'd', 'double']

def output_options(player: Player, num_turn: int):
    if (player.hand[0].worth == player.hand[1].worth):
        print("Type 'sp' or 'split' to split")
    print("Type 'h' or 'hit' to hit")
    print("Type 's' or 'stand' to stand")
    print("Type 'd' or 'double' to double down")

def output_initial_game_state(dealer: Dealer, player: Player):
    print("the dealer was dealt a:")
    for card in dealer.hand:
        card.print_card()
    print("his score is a", dealer.score)

    print("you were dealt a:")
    for card in player.hand:
        card.print_card()
    print("your score is a", player.score)

def deal_card_from(deck: list[Card]) -> Card:
    return deck.pop()

def deal_to_player(player_to_deal: Player, deck_to_deal_from: list[Card]):
    top_card = deal_card_from(deck_to_deal_from)
    player_to_deal.score += top_card.worth
    if player_to_deal.score > 21:
        player_to_deal.has_bust = True
    player_to_deal.hand.append(top_card)

def deal_to_dealer(dealer: Dealer, deck_to_deal_from: list[Card]):
    top_card = deal_card_from(deck_to_deal_from)
    dealer.score += top_card.worth
    if dealer.score > 21:
        dealer.has_bust = True
    dealer.hand.append(top_card)

def begin_game():
    deal_to_player(player_1, master_deck)
    deal_to_dealer(the_dealer, master_deck)
    deal_to_player(player_1, master_deck)
    deal_to_dealer(the_dealer, master_deck)
    output_initial_game_state(the_dealer, player_1)

def mid_game(player: Player, dealer: Dealer):
    while not player.has_bust and not dealer.has_bust: # while neither player or dealer has bust    
        output_options(player_1)
        user_move = ask_input("What would you like to do now?", ['sp', 'split', 'h', 'hit', 's', 'stand', 'd', 'double'])
        if user_move == 'h' or user_move == 'hit':
            print("You chose to hit!")
            deal_to_player(player_1)
begin_game() # only run once
mid_game(player_1, the_dealer)