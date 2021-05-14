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
        

def main():
    """
    """
    game = Game()
    print(game.wordselection.word_bag)


if __name__ == "__main__":
    main()
