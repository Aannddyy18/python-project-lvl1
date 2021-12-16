"""Search for missed number in the progression."""
from random import randint
from random import choice


def game_question():
    """Let's calculate."""
    rule = ('What number is missing in the progression?')
    start_progression = randint(1, 3)
    step_progression = randint(1, 3)
    end_progression = 16
    progression = range(start_progression, end_progression, step_progression)
    hidden = choice(progression)
    task = task_progression(progression, hidden)
    return (rule, task, hidden)


def task_progression(progression, number):
    """Forming progression."""
    i = 0
    s = ""
    for num in progression:
        if (progression[i] == number):
            s = s + ('..') + (" ")
        else:
            s = s + str(progression[i]) + (" ")
        i += 1
    return s
