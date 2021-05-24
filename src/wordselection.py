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
import copy


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
        self.word_structure = list()
        self.farsi = ''

    def __str__(self):
        """__str__ - string representation
        """
        print(f'{self.file_name=}')

    def __repr__(self):
        """__repr__ - representative
        """
        return "blah"

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
        # TODO: whatif word_bag isn't populated?  Throw something
        if not self.word_bag:
            raise ValueError
        farsi = random.choice(list(self.word_bag))
        english, english_desc = self.word_bag[farsi]
        self.farsi = farsi
        self.create_word_structure()
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
        # TODO: k=k problem when length of word_bag is < k
        picks = [temp_word_bag[word_key][0] for word_key in
                 random.sample(list(temp_word_bag), k=k)]
        return picks

    def check_guess(self, guess_letter):
        """check_guess

        :param:  guess_letter - the letter being guessed
        :return: result - True (correct) or False (incorrect)
        """
        return guess_letter in self.farsi

    def update_guessing(self, correct_letter):
        """update_guessing

        :param:  correct_letter
        :return: n/a
        """
        pass

    def create_word_structure(self):
        """create_word_structure
        """
        self.word_structure = [{k: ''} for k in self.farsi]

    def output_word_structure(self):
        """ create_word_structure

        This works for generating ABJAD output but LATIN is reversed.

        Right now the intent is for ABJAD based character sets so I'm
        leaving it here but put in a TODO to deal with potential
        future work to make it all pretty.
        """
        # TODO: regsubs?
        # TODO: need code to handle ABJAD vs LATIN (eventually)
        output = ""
        tmp = copy.deepcopy(self.word_structure)
        for key_pair in tmp:
            (key, value), = key_pair.items()
            if key == ' ':
                output += ' - '
                continue
            if value:
                output = f' {value} ' + output
            else:
                output = ' _ ' + output
        return output

    def update_word_structure(self, letter):
        """update_word_structure
        """
        # TODO: make this into a comprhension
        tmp = list()
        for pair in self.word_structure:
            (k, v), = pair.items()
            if k == letter:
                tmp.append({k: letter})
            else:
                tmp.append({k: v})
        self.word_structure = copy.deepcopy(tmp)

    def word_solved(self):
        """word_solved - checks if solved

        The word is considered to be solved if all
        values in the word structure are filled out.
        """
        # TODO: there is probably a pythonic way to do this
        rc = True
        for pair in self.word_structure:
            (k, v), = pair.items()
            if v == '':
                rc = False
        return rc


def main(arguments):
    """
    """
    x = WordSelection(arguments)
    x.read_file()
    y = x.pick_word_group()
    print(x.pick_some_english(y))
    x.create_word_structure()
    print(x.output_word_structure())
    print(x.farsi)


if __name__ == "__main__":
    main('../data/nouns.txt')
