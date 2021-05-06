#!/usr/bin/env python3
"""
"""
import sys
import csv


class WordSelection(object):
    """
    """
    def __init__(self, arguments):
        """
        """
        self.file_name = arguments

    def __str__(self):
        """
        """
        print(f'{self.file_name=}')

    def __repr__(self):
        """
        """
        return print(f'{self}')

    def read_list(self):
        """
        """
        with open(self.file_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                print(', '.join(row))


def main(arguments):
    """
    """
    x = WordSelection(arguments)
    x.read_list()


if __name__ == "__main__":
    main('../data/nouns.txt')
