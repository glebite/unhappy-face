import unittest
import unhappy


BIGNUMBEROFPIECES = 13


class Testing(unittest.TestCase):
    def test_creation(self):
        x = unhappy.Unhappy()
        self.assertNotEqual(x, None)

    def test_creation_pieces_set(self):
        x = unhappy.Unhappy(BIGNUMBEROFPIECES)
        self.assertEqual(x.n_pieces, BIGNUMBEROFPIECES)


if __name__ == '__main__':
    unittest.main()
