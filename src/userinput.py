#!/usr/bin/env python3
"""
"""
CHARACTERS = {'ا': 'alef',
              'ب': 'be',
              'پ': 'pe',
              'ت': 'te',
              'ث': 'se',
              'ج': 'jim',
              'چ': 'che',
              'ح': 'he',
              'خ': 'khe',
              'د': 'dal',
              'ذ': 'zal',
              'ر': 're',
              'ز': 'ze',
              'ژ': 'zhe',
              'س': 'sin',
              'ش': 'shin',
              'ص': 'sad',
              'ض': 'zad',
              'ط': 'ta',
              'ظ': 'za',
              'ع': 'ayn',
              'غ': 'gayn',
              'ف': 'fe',
              'ق': 'qaf',
              'ک': 'kaf',
              'گ': 'gaf',
              'ل': 'lam',
              'م': 'mim',
              'ن': 'nun',
              'و': 'vav',
              'ه': 'he',
              'ی': 'ye'}


class UserInput(object):
    """UserInput
    """
    def __init__(self):
        """__init__
        """
        self.character_set = CHARACTERS.copy()

    def prompt(self):
        """prompt - basic user input prompt

        This prompt function does no checks on the input for
        now so it is conceivable to enter nothing.

        :return: userinput
        """
        # TODO: fix null input
        print('Enter user input: ')
        userinput = input()
        print(f'User chose: {userinput}')
        return userinput

    def display_characters(self):
        """display_characters - returns the character_set

        :return: string with self.character_set
        """
        return f'{self.character_set}'

    def remove_character(self, character):
        """remove_character - removes a character from the charset

        :param:  character
        :raise:  KeyError if character not in character_set
        """
        try:
            self.character_set.pop(character)
        except ValueError:
            print(f'{character} is not in current charset:'
                  f' {self.character_set}')
        except KeyError:
            raise KeyError


def main():
    """main - stub for running as a tool/quick test
    """
    x = UserInput()
    x.display_characters()
    x.remove_character('ه')
    x.display_characters()


if __name__ == "__main__":
    main()
