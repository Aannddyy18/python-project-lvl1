"""Ask&Play."""


import prompt
from random import randint


def play_with_user():
    """Conversation."""
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    i = 1
    while i < 4:
        number = randint(1, 99)
        print('Question: {a}'.format(a=number))
        answer = prompt.secret('')
        print('Your answer: {a}'.format(a=answer))
        if ((answer == 'yes' and number % 2 == 0)
                or (answer == 'no' and number % 2 == 1)):
            print('Correct!')
            if i == 3:
                print('Congratulations, {a}!'.format(a=name))
        elif (answer != 'no' and number % 2 == 1):
            print('{a} is wrong answer ;(.'
                  ' Correct answer was \'no\'.'.format(a=answer))
            print('Let\'s try again, {a}!'.format(a=name))
            break
        elif (answer != 'yes' and number % 2 == 0):
            print('{a} is wrong answer ;(.'
                  ' Correct answer was \'yes\'.'.format(a=answer))
            print('Let\'s try again, {a}!'.format(a=name))
            break
        i += 1
