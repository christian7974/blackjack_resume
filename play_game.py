"""
Functions for gameplay are created here; this is the file where all of the gameplay will occur
"""
from start_game import Card, player_1, master_deck, the_dealer
from player import Player
from dealer import Dealer
from helpers import ask_input
user_options_first_turn = ['sp', 'split', 'h', 'hit', 's', 'stand', 'd', 'double'] # you can only choose to split on the first turn
user_options_subsequent_turn = ['h', 'hit', 's', 'stand', 'd', 'double']

def output_options(player: Player, num_turn: int):
    if (player.hand[0].worth == player.hand[1].worth) and num_turn == 0:
        print("Type 'sp' or 'split' to split")
    print("Type 'h' or 'hit' to hit")
    print("Type 's' or 'stand' to stand")
    print("Type 'd' or 'double' to double down")

def deal_card_from(deck: list[Card]) -> Card:
    return deck.pop()

def deal_to_player(player_to_deal: Player, deck_to_deal_from: list[Card]):
    top_card = deal_card_from(deck_to_deal_from)
    print("You have been dealt ", end='')
    top_card.print_card()
    player_to_deal.score += top_card.worth
    if player_to_deal.score > 21:
        player_to_deal.has_bust = True
    player_to_deal.hand.append(top_card)

def deal_to_dealer(dealer: Dealer, deck_to_deal_from: list[Card]):
    top_card = deal_card_from(deck_to_deal_from)
    print("The dealer was dealt ", end='')
    top_card.print_card()
    dealer.score += top_card.worth
    if dealer.score > 21:
        dealer.has_bust = True
    dealer.hand.append(top_card)
# TODO: THE USER IS PRESENTED WITH THE OPTION TO SPLIT, HOWEVER WHEN CHOSEN THEY ARE UNABLE TO DO SO
def game_play():
    num_turn = 0
    deal_to_player(player_1, master_deck)
    deal_to_dealer(the_dealer, master_deck)
    deal_to_player(player_1, master_deck)
    print("-----------------------")
    print("You have a score of", player_1.score)
    print("The dealer has a score of", the_dealer.score)
    print("-----------------------")
    if (player_1.score == 21):
        print("You have Blackjack! It is the dealer's turn!")
        dealer_deals()
    else: 
        while (player_1.score <= 21):
            output_options(player_1, num_turn)
            num_turn += 1
            user_move = ask_input("What would you like to do now?", user_options_subsequent_turn)
            if user_move == 'h' or user_move == 'hit':
                deal_to_player(player_1, master_deck)
                print("-----------------------")
                print("You have a score of", player_1.score)

            elif user_move == 's' or user_move == 'stand':
                print("You chose to stand! It is the dealer's turn!")
                dealer_deals()
                break

            elif user_move == 'd' or user_move == 'double':
                print("You chose to double down!")
                deal_to_player(player_1, master_deck)
                print("-----------------------")
                print("You have a score of", player_1.score)
                print("It is the dealer's turn!")
                dealer_deals()
                break
                
            if (player_1.score > 21):
                print("The player has bust with a score of", player_1.score)
                player_1.has_bust = True
                break

    check_for_winner()

def dealer_deals():
    while (the_dealer.score < 17):
        deal_to_dealer(the_dealer, master_deck)
        print("-----------------------")
        print("The dealer has a score of", the_dealer.score)
        if (the_dealer.score > 21):
            print("The dealer has bust with a score of", the_dealer.score)
            the_dealer.has_bust = True

def check_for_winner():
    print("-----------------------")
    print("You have a score of", player_1.score)
    print("The dealer has a score of", the_dealer.score)
    print("-----------------------")
    if (player_1.has_bust):
        if (not the_dealer.has_bust):
            print("The dealer has won because you bust!")
        else:
            print("Neither of you won; Push")
    elif (the_dealer.has_bust):
        if (not player_1.has_bust):
            print("You won because the dealer bust!")
    elif (not the_dealer.has_bust and not player_1.has_bust): # neither player bust; compare scores
        if the_dealer.score > player_1.score:
            print("The dealer won because they have a higher score!")
        elif the_dealer.score < player_1.score:
            print("You won because you have a higher score!")
        else: 
            print("Neither of you won; Push")