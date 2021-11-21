#!/usr/bin/env python3
"""Finding missed number in progression."""


from brain_games.games_engine import play_with_user
from brain_games.games import progression


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    play_with_user(progression)


if __name__ == '__main__':
    main()
