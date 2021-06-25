"""test_game.py

A much needed test for confirming that the basic game
engine works.
"""
import unittest
import game


class Testing(unittest.TestCase):
    def test_game_creation(self):
        x = game.Game()
        self.assertNotEqual(x, None)

    def test_random_word_selected(self):
        x = game.Game()
        self.assertNotEqual(x.word_group, None)


if __name__ == '__main__':
    unittest.main()
