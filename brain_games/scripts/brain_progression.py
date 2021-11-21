#!/usr/bin/env python3
 
"""Finding missed number in progression."""


from brain_games.games_engine import play_with_user
import brain_games.games.progression


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    play_with_user(brain_games.games.progression)


if __name__ == '__main__':
    main()
