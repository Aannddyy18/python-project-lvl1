"""Search for greatest common divisor of given numbers."""
from random import randint
from math import gcd


RULE = 'Find the greatest common divisor of given numbers.'


def calculate():
    """Let's calculate."""
    MIN_NUMBER = 1
    MAX_NUMBER = 99
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    gr_divisor = gcd(first_number, second_number)
    task = ('{a} {b}'.format(a=first_number, b=second_number))
    return task, gr_divisor
