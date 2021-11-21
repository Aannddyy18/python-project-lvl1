"""Search for missed number in the progression."""
from random import randint
from random import choice


def main_question():
    """Question."""
    print('What number is missing in the progression?')


def game_question():
    """Let's calculate."""
    start = randint(1, 3)
    step = randint(1, 3)
    progr = range(start, 16, step)
    hidden = choice(progr)
    print('Question:', end=" ")
    print_progr(progr, hidden)
    return hidden


def print_progr(progress, randomnumber):
    """Print progression."""
    i = 0
    for num in progress:
        if (progress[i] == randomnumber):
            print('..', end=" ")
        else:
            print(progress[i], end=" ")
        i += 1
    print()
