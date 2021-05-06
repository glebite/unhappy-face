#!/usr/bin/env python3
"""
"""
import sys
import csv
import random


class WordSelection(object):
    """
    """
    def __init__(self, arguments):
        """
        """
        self.file_name = arguments
        self.word_bag = dict()

    def __str__(self):
        """
        """
        print(f'{self.file_name=}')

    def __repr__(self):
        """
        """
        return print(f'{self}')

    def read_file(self):
        """read_file - reads a .csv file filled with words

        Word list files are in .csv (, comma) delimitered according to:
        English, Farsi, English Description
        ...
        EOF

        A dictionary is created from the column values with end whitespaces
        stripped as part of the data cleaning:
        Farsi: (English, English Description)

        param:  None
        return: None
        """
        with open(self.file_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            self.word_bag = {r[1].strip(): (r[0].strip(), r[2].strip())
                             for r in reader}
        print(self.word_bag)

    def pick_word(self):
        pass


def main(arguments):
    """
    """
    x = WordSelection(arguments)
    x.read_file()


if __name__ == "__main__":
    main('../data/nouns.txt')
