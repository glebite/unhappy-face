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
        """
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
        """run
        """
        # print(f'Word: {self.word_group}')

        while self.ingame:
            # print(self.userinput.display_characters())
            print(f'Word: {self.word_group}')
            print(f'Something: {self.wordselection.word_structure}')
            print(self.wordselection.output_word_structure())
            command = self.userinput.prompt()
            if command == "quit":
                self.ingame = False
            elif command == "reset":
                self.ingame = False
            else:
                if command in self.word_group[0]:
                    print(f'{command} found!')
                    self.wordselection.update_word_structure(command)
                    self.game.incr_stat('correct letters')
                else:
                    print(f'{command} not found!')
                    self.game.incr_stat('incorrect letters')
                    self.unhappy.incr()
                self.userinput.remove_character(command)
            if self.wordselection.word_solved():
                print('Yay you win!')
                self.ingame = False
                print(self.game.stats)
            if self.game.stats['incorrect letters'] == unhappy.NORMALGAME:
                print('Boo you lose!')
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
