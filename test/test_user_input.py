import unittest
import userinput


class Testing(unittest.TestCase):
    def test_creation(self):
        x = userinput.UserInput()
        self.assertNotEqual(x, None)

    def test_charset_initialization(self):
        x = userinput.UserInput()
        self.assertEqual(x.character_set, userinput.CHARACTERS)

    def test_charset_display(self):
        x = userinput.UserInput()
        self.assertEqual(str(x.character_set), str(x.display_characters()))

    def test_charset_remove(self):
        x = userinput.UserInput()
        # my favourite character :)
        x.remove_character('پ')
        self.assertNotIn('پ', x.character_set)

    def test_charset_remove_missing(self):
        x = userinput.UserInput()
        # my favourite character :)
        try:
            x.remove_character('+')
            self.assertFalse(False)
        except KeyError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
