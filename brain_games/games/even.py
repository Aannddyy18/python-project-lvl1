"""Even-uneven game."""

from random import randint


RULE = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
MIN_NUMBER = 1
MAX_NUMBER = 99


def form_task_and_answer():
    """Let's play."""
    number = randint(MIN_NUMBER, MAX_NUMBER)
    task = ('{a}'.format(a=number))
    even_number = (number % 2 == 0)
    if even_number:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return task, right_answer
