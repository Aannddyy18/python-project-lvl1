#!/usr/bin/env python3
 
"""Calculator game."""


from brain_games.games_engine import play_with_user
import brain_games.games.calc


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    play_with_user(brain_games.games.calc)


if __name__ == '__main__':
    main()
