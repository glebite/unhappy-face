import unittest
import wordselection


class Testing(unittest.TestCase):
    def test_creation(self):
        x = wordselection.WordSelection('nonce')
        self.assertNotEqual(x, None)


if __name__ == '__main__':
    unittest.main()
