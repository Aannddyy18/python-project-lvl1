"""Game's routine."""

import prompt


def play_with_user(game):
    """Conversation."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
    i = 1
    while i < 4:
        (game_rules, task, result) = game.game_question()
        print(game_rules)
        print('Question:', task)
        answer = prompt.string('Your answer: ')
        if (str(result) == answer):
            print('Correct!')
            if i == 3:
                print('Congratulations, {a}!'.format(a=name))
        else:
            print('\'{a}\' is wrong answer ;(.'
                  ' Correct answer was \'{b}\'.'.format(a=answer, b=result))
            print('Let\'s try again, {a}!'.format(a=name))
            break
        i += 1
