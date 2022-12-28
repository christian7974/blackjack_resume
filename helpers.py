"""
File for other functions that did not fit into the other files (such as asking for input)
"""

"""
Function that can ask the user for input and checks if it is a possible value; runs until a valid input is inputted from the user
Args:
    question_to_ask (str): the question that needs to be asked
    possible_values (list of str): valid answer(s) to the question

Returns:
    str: the valid input to the question
"""
def ask_input(question_to_ask: str, valid_answers: list):
    while True:
        answer_to_question = input(question_to_ask + " ").lower()
        if answer_to_question in valid_answers:
            return answer_to_question