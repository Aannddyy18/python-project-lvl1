"""Even-uneven game."""

from random import randint


def game_question():
    """Let's play."""
    rules = ('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    number = randint(1, 99)
    task = ('{a}'.format(a=number))
    even_number = (number % 2 == 0)
    if even_number:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (rules, task, right_answer)
