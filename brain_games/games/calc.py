"""Calculator game."""

from random import randint
from random import choice


RULE = 'What is the result of the expression?'


def calculate():
    """Let's calculate."""
    MIN_NUMBER = 1
    MAX_NUMBER = 99
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    sign = choice('+-*')
    task = ('{a} {b} {c}'.format(a=first_number, b=sign, c=second_number))
    if sign == '+':
        result = first_number + second_number
    elif sign == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return task, result
