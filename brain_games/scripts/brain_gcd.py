#!/usr/bin/env python3
"""Greatest common divisor game."""


from brain_games.games_engine import play_with_user
from brain_games.games import gcd


def main():
    play_with_user(gcd)


if __name__ == '__main__':
    main()
