"""Search for missed number in the progression."""
from random import randint


RULE = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 3
MIN_STEP = 1
MAX_STEP = 3
QUANTITY_ELEM = 15


def form_task_and_answer():
    """Let's calculate."""
    progression, hidden_index, hidden = form_progression()
    task = stringify_progression(progression, hidden_index)
    return task, hidden


def form_progression():
    start_progression = randint(MIN_START, MAX_START)
    step_progression = randint(MIN_STEP, MAX_STEP)
    progression = range(start_progression, QUANTITY_ELEM + 1, step_progression)
    hidden_index = randint(0, len(progression) - 1)
    hidden = progression[hidden_index]
    return progression, hidden_index, hidden


def stringify_progression(progression, hidden_index):
    """Forming progression."""
    progression = list(progression)
    return " ".join(str(s) if i != hidden_index else ".." for i,
                    s in enumerate(progression))
