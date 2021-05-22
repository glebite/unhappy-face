import unittest
import userinput


class Testing(unittest.TestCase):
    def test_creation(self):
        x = userinput.UserInput()
        self.assertNotEqual(x, None)

    def test_charset_initialization(self):
        x = userinput.UserInput()
        self.assertEqual(x.character_set, userinput.CHARACTERS)

    def test_charset_remove(self):
        x = userinput.UserInput()
        # my favourite character :)
        x.remove_character('پ')
        self.assertNotIn('پ', x.character_set)


if __name__ == '__main__':
    unittest.main()
