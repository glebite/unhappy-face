import unittest
import gamecore


class Testing(unittest.TestCase):
    def test_creation(self):
        x = gamecore.GameCore('nonce')
        self.assertNotEqual(x, None)


if __name__ == '__main__':
    unittest.main()
