"""Prime number game."""

from random import randint


def main_question():
    """Question."""
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')


def game_question():
    """Let's play."""
    number = randint(1, 99)
    print('Question: {a}'.format(a=number))
    if IsPrime(number):
        return 'yes'
    else:
        return 'no'


def IsPrime(n):
    """Check if number is prime."""
    d = 2
    while n % d != 0:
        d += 1
    return d == n
