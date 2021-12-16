"""Search for greatest common divisor of given numbers."""
from random import randint
from math import gcd


def game_question():
    """Let's calculate."""
    rule = ('Find the greatest common divisor of given numbers.')
    first_number = randint(1, 99)
    second_number = randint(1, 99)
    nod = gcd(first_number, second_number)
    task = ('{a} {b}'.format(a=first_number, b=second_number))
    return (rule, task, nod)
