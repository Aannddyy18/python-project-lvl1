"""Search for missed number in the progression."""
from random import randint


RULE = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 3
MIN_STEP = 1
MAX_STEP = 3
QUANTITY_ELEM = 10


def form_task_and_answer():
    """Let's calculate."""
    initial_term = randint(MIN_START, MAX_START)
    common_difference = randint(MIN_STEP, MAX_STEP)
    end_term = (initial_term + common_difference * (QUANTITY_ELEM - 1))
    progression = form_progression(initial_term, end_term, common_difference)
    hidden_index = randint(0, QUANTITY_ELEM - 1)
    hidden = progression[hidden_index]
    task = stringify_progression(progression, hidden_index)
    return task, hidden


def form_progression(initial_term, end_term, common_difference):
    progression = range(initial_term, end_term + 1, common_difference)
    return progression


def stringify_progression(progression, hidden_index):
    """Forming progression."""
    progression = list(progression)
    return " ".join(str(s) if i != hidden_index else ".." for i,
                    s in enumerate(progression))
