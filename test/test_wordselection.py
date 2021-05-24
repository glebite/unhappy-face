import unittest
import wordselection

WORD_GROUP_PICK = 3


class Testing(unittest.TestCase):
    def test_creation(self):
        x = wordselection.WordSelection('nonce')
        self.assertNotEqual(x, None)

    def test_confirm_arguments(self):
        x = wordselection.WordSelection('nonce')
        self.assertEqual(x.file_name, 'nonce')

    def test_confirm_farsi_empty(self):
        x = wordselection.WordSelection('nonce')
        self.assertEqual(x.farsi, '')

    def test_confirm_check_guess(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = ' شهر'
        self.assertEqual(x.check_guess('ه'), True)

    def test_confirm_check_guess_false(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = ' شهر'
        self.assertEqual(x.check_guess('a'), False)

    def test_word_structure(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        test_structure = [{'a': ''}, {'b': ''}, {'c': ''}]
        x.create_word_structure()
        self.assertEqual(x.word_structure, test_structure)

    def test_output_word_structure(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        expected_output = " _  _  _ "
        self.assertEqual(x.output_word_structure(), expected_output)

    def test_word_not_solved(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        self.assertEqual(x.word_solved(), False)

    def test_word_solved(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        x.word_structure = [{'a': 'a'}, {'b': 'b'}, {'c': 'c'}]
        self.assertEqual(x.word_solved(), True)

    def test_word_partially_solved(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        x.word_structure = [{'a': 'a'}, {'b': ''}, {'c': 'c'}]
        self.assertEqual(x.word_solved(), False)

    def test_incremental_building(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'پنجره'
        x.create_word_structure()
        empty_compare = [{'پ': ''}, {'ن': ''},
                         {'ج': ''}, {'ر': ''}, {'ه': ''}]
        full_compare = [{'پ': 'پ'}, {'ن': 'ن'},
                        {'ج': 'ج'}, {'ر': 'ر'}, {'ه': 'ه'}]
        self.assertEqual(x.word_structure, empty_compare)
        for keypair in empty_compare:
            (key, value), = keypair.items()
            x.update_word_structure(key)
        self.assertEqual(x.word_structure, full_compare)

    def test_reverse_building(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'پنجره'
        x.create_word_structure()
        empty_compare = [{'پ': ''}, {'ن': ''},
                         {'ج': ''}, {'ر': ''}, {'ه': ''}]
        full_compare = [{'پ': 'پ'}, {'ن': 'ن'},
                        {'ج': 'ج'}, {'ر': 'ر'}, {'ه': 'ه'}]
        self.assertEqual(x.word_structure, empty_compare)
        for keypair in empty_compare[::-1]:
            (key, value), = keypair.items()
            x.update_word_structure(key)
        self.assertEqual(x.word_structure, full_compare)

    def test_quick_pick_word_group(self):
        x = wordselection.WordSelection('../data/nouns.txt')
        x.read_file()
        word_group = x.pick_word_group()
        self.assertTrue(len(word_group))

    def test_confirm_pick_word_handles_empty(self):
        x = wordselection.WordSelection('../data/nouns.txt')
        with self.assertRaises(ValueError) as context:
            word_group = x.pick_word_group()
        self.assertTrue(context.exception)

    def test_pick_some_default(self):
        x = wordselection.WordSelection('../data/nouns.txt')
        x.read_file()
        word_group = x.pick_word_group()
        picks = x.pick_some_english(word_group)
        self.assertEqual(len(picks), wordselection.PICK_ENGLISH)

    def test_pick_some_number(self):
        x = wordselection.WordSelection('../data/nouns.txt')
        x.read_file()
        word_group = x.pick_word_group()
        picks = x.pick_some_english(word_group, k=WORD_GROUP_PICK)
        self.assertEqual(len(picks), WORD_GROUP_PICK)

    def test_read_file_happy(self):
        x = wordselection.WordSelection('../data/nouns.txt')
        try:
            x.read_file()
            self.assertTrue(True)
        except FileNotFoundError as e:
            print(f'This has failed because: {e}')
            self.assertFalse(True)

    def test_read_file_bad(self):
        x = wordselection.WordSelection('../data/nounsdonotexist.txt')
        try:
            x.read_file()
            self.assertFalse(True)
        except FileNotFoundError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
