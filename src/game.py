#!/usr/bin/env python3
"""
"""
import gamecore
import unhappy
import wordselection


class Game(object):
    """
    """
    def __init__(self):
        """
        """
        self.game = gamecore.GameCore('')
        self.unhappy = unhappy.Unhappy()
        # TODO: move to configuration or such..
        self.wordselection = wordselection.WordSelection('../data/nouns.txt')
        self.wordselection.read_file()
        word_group = (self.wordselection.pick_word_group())
        for x in word_group[0]:
            print(f'letter: {x}')
        if x in word_group[0]:
            print(f'Yes, {x} is in {word_group[0]}')


def main():
    """
    """
    game = Game()


if __name__ == "__main__":
    main()
