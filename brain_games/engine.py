"""Game's routine."""

import prompt


NUMBER_OF_ROUNDS = 3


def play_with_user(game):
    """Conversation."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
    print(game.RULE)
    for i in range(NUMBER_OF_ROUNDS):
        task, true_answr = game.form_task_and_answer()
        print('Question:', task)
        answer = prompt.string('Your answer: ')
        if str(true_answr) == answer:
            print('Correct!')
        else:
            print('\'{a}\' is wrong answer ;(.'
                  ' Correct answer was \'{b}\'.'.format(a=answer, b=true_answr))
            print('Let\'s try again, {a}!'.format(a=name))
            return
    print('Congratulations, {a}!'.format(a=name))
