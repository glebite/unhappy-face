import unittest
import wordselection


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


if __name__ == '__main__':
    unittest.main()
