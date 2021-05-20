import unittest
import unhappy


class Testing(unittest.TestCase):
    def test_creation(self):
        x = unhappy.Unhappy()
        self.assertNotEqual(x, None)

if __name__ == '__main__':
    unittest.main()
