"""
If the player has never played Blackjack before, then this file will present the rules required to play
"""
def retrieve_from_rules_file():
    rules_file = open("rules.md", "r")
    line_in_file = rules_file.readline()
    line_in_file = line_in_file.replace('#', '')
    print(line_in_file)
    while line_in_file != '':
        line_in_file = rules_file.readline()
        line_in_file = line_in_file.replace('*', '')
        print(line_in_file)
    rules_file.close()