#!/usr/bin/env python3

"""Prime number game."""


from brain_games.games_engine import play_with_user
from brain_games.games import prime


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    play_with_user(prime)


if __name__ == '__main__':
    main()