"""Search for greatest common divisor of given numbers."""
 
from random import randint
from math import gcd


def main_question():
    """Question."""
    print('Find the greatest common divisor of given numbers.')


def game_question():
    """Let's calculate."""
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    nod = gcd(number_one, number_two)
    print('Question: {a} {b}'.format(a=number_one, b=number_two))
    return nod
