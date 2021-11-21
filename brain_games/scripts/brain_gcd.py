#!/usr/bin/env python3
 
"""Greatest common divisor game."""


from brain_games.games_engine import play_with_user
from brain_games.games import gcd_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    play_with_user(gcd_game)


if __name__ == '__main__':
    main()
