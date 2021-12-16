"""Prime number game."""

from random import randint


def game_question():
    """Let's play."""
    rule = ('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    number = randint(1, 99)
    task = ('{a}'.format(a=number))
    result = ""
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    return (rule, task, result)


def is_prime(n):
    """Check if number is prime."""
    d = 2
    while n % d != 0:
        d += 1
    return d == n
