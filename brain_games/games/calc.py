"""Calculator game."""

from random import randint
from random import choice


def main_question():
    """Question."""
    print('What is the result of the expression?')


def game_question():
    """Let's calculate."""
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    sign = choice('+-*')
    print('{a} {b} {c}'.format(a=number_one, b=sign, c=number_two))
    if sign == '+':
        result = number_one + number_two
    elif sign == '-':
        result = number_one - number_two
    else:
        result = number_one * number_two
    return result
