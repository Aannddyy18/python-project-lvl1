"""Calculator game."""

from random import randint
from random import choice


def game_question():
    """Let's calculate."""
    game_rules = 'What is the result of the expression?'
    first_number = randint(1, 99)
    second_number = randint(1, 99)
    sign = choice('+-*')
    task = ('{a} {b} {c}'.format(a=first_number, b=sign, c=second_number))
    if sign == '+':
        result = first_number + second_number
    elif sign == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return (game_rules, task, result)
