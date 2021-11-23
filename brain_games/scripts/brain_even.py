#!/usr/bin/env python3
"""Even-uneven game."""


from brain_games.games_engine import play_with_user
from brain_games.games import even


def main():
    play_with_user(even)


if __name__ == '__main__':
    main()
