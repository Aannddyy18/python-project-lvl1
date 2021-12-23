#!/usr/bin/env python3

"""Calculator game."""


from brain_games.engine import play_with_user
from brain_games.games import calc


def main():
    play_with_user(calc)


if __name__ == '__main__':
    main()
