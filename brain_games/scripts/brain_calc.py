#!/usr/bin/env python3

"""Calculator game."""


from brain_games.games_engine import play_with_user
from brain_games.games import calc


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    play_with_user(calc)


if __name__ == '__main__':
    main()
