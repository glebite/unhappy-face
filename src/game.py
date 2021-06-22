#!/usr/bin/env python3
"""
"""
import gamecore
import unhappy
import wordselection
import userinput


class Game(object):
    """
    """
    def __init__(self):
        """__init__
        """
        self.game = gamecore.GameCore('')
        self.unhappy = unhappy.Unhappy()
        self.userinput = userinput.UserInput()
        # TODO: move to configuration or such..
        self.wordselection = wordselection.WordSelection('../data/nouns.txt')
        self.wordselection.read_file()
        self.word_group = (self.wordselection.pick_word_group())
        self.ingame = True

    def run(self):
        """run - main run engine
        """
        # TODO: refactor this okay, pumpkin?
        while self.ingame:
            print(self.userinput.display_characters())
            print(self.wordselection.output_word_structure())
            command = self.userinput.prompt()
            if command == "quit":
                self.ingame = False
            elif command == "reset":
                self.ingame = False
            else:
                if self.wordselection.check_guess(command):
                    print(f'{command} found!')
                    self.wordselection.update_word_structure(command)
                    self.game.incr_stat('correct letters')
                else:
                    print(f'{command} not found!')
                    self.game.incr_stat('incorrect letters')
                    self.unhappy.incr()
                try:
                    self.userinput.remove_character(command)
                except KeyError:
                    print(f'{command} is not in the set - you'
                          ' will not be punished.')
                    continue
            if self.wordselection.word_solved():
                print('Yay you win!')
                print(self.wordselection.output_word_structure()[::-1])
                print(f'The word was: {self.word_group[0]}')
                self.ingame = False
                print(self.game.stats)
            if self.game.stats['incorrect letters'] == unhappy.NORMALGAME:
                print('Boo you lose!')
                print(f'\tThe word was: {self.word_group[0]}')
                self.ingame = False
                print(self.game.stats)
            if self.game.stats['incorrect letters']:
                print('Draw unhappy bits...')
                self.unhappy.draw()


def main():
    """
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
