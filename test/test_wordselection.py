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


if __name__ == '__main__':
    unittest.main()
