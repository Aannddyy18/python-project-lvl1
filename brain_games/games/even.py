"""Even-uneven game."""

from random import randint


def main_question():
    """Question."""
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')


def game_question():
    """Let's play."""
    number = randint(1, 99)
    print('{a}'.format(a=number))
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
