"""Asking."""


import prompt


def welcome_user():
    """Conversation."""
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
