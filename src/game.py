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
        print(f'Word: {self.word_group}')

        while self.ingame:
            print(self.wordselection.output_word_structure())
            command = self.userinput.prompt()
            if command == "quit":
                self.ingame = False
            elif command == "solve":
                self.ingame = False
            else:
                if command in self.word_group[0]:
                    print(f'{command} found!')
                    self.wordselection.update_word_structure(command)
                else:
                    print(f'{command} not found!')
            if self.wordselection.word_solved():
                print(f'Yay you win!')
                self.ingame = False


def main():
    """
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
