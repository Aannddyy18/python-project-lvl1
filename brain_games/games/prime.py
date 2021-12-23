"""Prime number game."""

from random import randint


RULE = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def calculate():
    """Let's play."""
    MIN_NUMBER = 1
    MAX_NUMBER = 99
    number = randint(MIN_NUMBER, MAX_NUMBER)
    task = ('{a}'.format(a=number))
    result = ""
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    return task, result


def is_prime(n):
    """Check if number is prime."""
    d = 2
    while n % d != 0:
        d += 1
    return d == n
