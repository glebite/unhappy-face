#!/usr/bin/env python3
"""
"""
import sys


class GameCore(object):
    """GameCore - unhappy face game core - stats, etc...
    """
    def __init__(self, arguments):
        """__init__

        param:  arguments - configuration args (TBD)
        """
        self.stats = {'win': 0,
                      'lose': 0,
                      'games': 0,
                      'correct letters': 0,
                      'incorrect letters': 0}

    def __str__(self):
        """__str__ string output """
        return f'{self.stats}'

    def __repr__(self):
        """__repr__ represent"""
        return f'{self}'

    def incr_stat(self, stat):
        if stat in self.stats:
            self.stats[stat] += 1
        else:
            raise ValueError


def main(arguments):
    """main - launcher if executed as a tool

    param:  arguments - essentially sys.argv
    return: None
    """
    game = GameCore(arguments)
    print(game)


if __name__ == "__main__":
    main(sys.argv)
