#!/usr/bin/env python3
"""
"""


class UserInput(object):
    """
    """
    def __init__(self):
        """__init__
        """
        pass

    def prompt_for_character(self):
        """prompt_for_character
        """
        print('Enter a character choice: ')
        character = input()
        print(f'User chose: {character}')


def main():
    """
    """
    user = UserInput()
    print(user)


if __name__ == "__main__":
    main()
