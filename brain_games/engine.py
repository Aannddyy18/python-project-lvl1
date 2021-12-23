"""Game's routine."""

import prompt


def play_with_user(game):
    """Conversation."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
    print(game.RULE)
    for i in range(3):
        (task, result) = game.calculate()
        print('Question:', task)
        answer = prompt.string('Your answer: ')
        if (str(result) == answer):
            print('Correct!')
        else:
            print('\'{a}\' is wrong answer ;(.'
                  ' Correct answer was \'{b}\'.'.format(a=answer, b=result))
            print('Let\'s try again, {a}!'.format(a=name))
            return
    print('Congratulations, {a}!'.format(a=name))
