#!/usr/bin/env python3
"""wordselection.py

So the idea is that this class/module will allow for the
reading in of a .csv file and the game can select the current_farsi_word
to be tried out, and upon success or failure, there is a method that
then allows for the second phase of the game where the user is prompted
to match the Farsi word with a list of english words!!!

Ultimately, this can be moved out to use other languages and such but
for now it will just be Farsi and English.
"""
import csv
import random


PICK_ENGLISH = 4


class WordSelection(object):
    """WordSelection
    """
    def __init__(self, arguments):
        """__init__ - create the WordSelection object

        param:  arguments
        return: n/a
        """
        self.file_name = arguments
        self.word_bag = dict()

    def __str__(self):
        """__str__ - string representation
        """
        print(f'{self.file_name=}')

    def __repr__(self):
        """__repr__ - representative 
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
            self.word_bag = {row[1].strip(): (row[0].strip(), row[2].strip())
                             for row in reader}
        return None

    def pick_word_group(self):
        """pick_word_group - randomly select a word to use

        param:  None
        return: list containing farsi, english, english def
        """
        farsi = random.choice(list(self.word_bag))
        english, english_desc = self.word_bag[farsi]
        return [farsi, english, english_desc]

    def pick_some_english(self, word_group, k=PICK_ENGLISH):
        """pick_some_english - find 'k' english words

        param:  word_group - the list returned from pick_word
        return: picks - a list of 'k' english words for comparison
        """
        temp_word_bag = self.word_bag
        # remove the current_farsi_word from our selection base
        temp_word_bag.pop(word_group[0])

        # temp_word_bag[word_key] is a tuple - we want the first entry
        picks = [temp_word_bag[word_key][0] for word_key in
                 random.sample(list(temp_word_bag), k=k)]
        return picks


def main(arguments):
    """
    """
    x = WordSelection(arguments)
    x.read_file()
    y = x.pick_word_group()
    print(x.pick_some_english(y))


if __name__ == "__main__":
    main('../data/nouns.txt')
