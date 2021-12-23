"""Search for missed number in the progression."""
from random import randint


RULE = 'What number is missing in the progression?'


def calculate():
    """Let's calculate."""
    MIN_START = 1
    MAX_START = 3
    start_progression = randint(MIN_START, MAX_START)
    MIN_STEP = 1
    MAX_STEP = 3
    step_progression = randint(MIN_STEP, MAX_STEP)
    END_PROGRESSION = 16
    progression = range(start_progression, END_PROGRESSION, step_progression)
    hidden_index = randint(0, len(progression) - 1)
    hidden = progression[hidden_index]
    task = make_progression(progression, hidden_index)
    return task, hidden


def make_progression(progression, hidden_index):
    """Forming progression."""
    progression = list(progression)
    for (i, elem) in enumerate(progression):
        if progression[i] == progression[hidden_index]:
            progression[hidden_index] = '..'
        else:
            progression[i] = str(elem)
    s = ' '.join(progression)
    return s
