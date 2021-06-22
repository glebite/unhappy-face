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
        """incr_stat - increment a given stat

        :param:  stat - the statistic to increment
        :return: n/a
        :raises: ValueError if the stat doesn't exist
        """
        if stat in self.stats:
            self.stats[stat] += 1
        else:
            raise ValueError

    def clear_stats(self):
        """clear_stats - clear out the game stats

        :param:  n/a
        :return: n/a
        :raise:  n/a
        """
        for key in self.stats.keys():
            self.stats[key] = 0


def main(arguments):
    """main - launcher if executed as a tool

    param:  arguments - essentially sys.argv
    return: None
    """
    game = GameCore(arguments)
    print(game)


if __name__ == "__main__":
    main(sys.argv)
