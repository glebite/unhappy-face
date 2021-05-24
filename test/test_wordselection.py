import unittest
import wordselection


class Testing(unittest.TestCase):
    def test_creation(self):
        x = wordselection.WordSelection('nonce')
        self.assertNotEqual(x, None)
        del x

    def test_confirm_arguments(self):
        x = wordselection.WordSelection('nonce')
        self.assertEqual(x.file_name, 'nonce')
        del x

    def test_confirm_farsi_empty(self):
        x = wordselection.WordSelection('nonce')
        self.assertEqual(x.farsi, '')
        del x

    def test_confirm_check_guess(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = ' شهر'
        self.assertEqual(x.check_guess('ه'), True)
        del x

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
        del x

    def test_output_word_structure(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        expected_output = " _  _  _ "
        self.assertEqual(x.output_word_structure(), expected_output)
        del x

    def test_word_not_solved(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        self.assertEqual(x.word_solved(), False)
        del x

    def test_word_solved(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        x.word_structure = [{'a': 'a'}, {'b': 'b'}, {'c': 'c'}]
        self.assertEqual(x.word_solved(), True)
        del x

    def test_word_partially_solved(self):
        x = wordselection.WordSelection('nonce')
        x.farsi = 'abc'
        x.create_word_structure()
        x.word_structure = [{'a': 'a'}, {'b': ''}, {'c': 'c'}]
        self.assertEqual(x.word_solved(), False)
        del x

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


if __name__ == '__main__':
    unittest.main()
