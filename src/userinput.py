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

    def prompt(self):
        """prompt
        """
        print('Enter user input: ')
        userinput = input()
        print(f'User chose: {userinput}')
        return userinput


def main():
    """
    """
    user = UserInput()
    print(user)
    user.prompt()


if __name__ == "__main__":
    main()
