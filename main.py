"""
Main file where the game gets started and everything required for the game (deck of cards, dealer and player) is initialized here.
"""
from helpers import *
from output_rules import retrieve_from_rules_file

valid_prelim_decision_answers: list[str] = ["p", "play","q", "quit", "rules", "r"]
first_question = "\nType 'p' or 'play' to start to play \nType 'r' or 'rules' to view the rules \nOr 'q' or 'quit' to start to quit"
def main():

    print("Welcome to Blackjack!", end="")
    print(first_question)
    
    prelim_decision: str = ask_input("What would you like to do now?", valid_prelim_decision_answers)
    while prelim_decision not in ["p", "play"]:
        if prelim_decision in ["r", "rules"]:
            retrieve_from_rules_file()
            print(first_question)

        if prelim_decision in ["q", "quit"]:
            quit()
        
        prelim_decision: str = ask_input("What would you like to do now?", valid_prelim_decision_answers)

    print("time to play!")
main()