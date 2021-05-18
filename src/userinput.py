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
