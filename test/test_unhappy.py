import unittest
import unhappy


BIGNUMBEROFPIECES = 13
BADNUMPIECES = 0


class Testing(unittest.TestCase):
    def test_creation(self):
        x = unhappy.Unhappy()
        self.assertNotEqual(x, None)

    def test_creation_pieces_set(self):
        x = unhappy.Unhappy(BIGNUMBEROFPIECES)
        self.assertEqual(x.n_pieces, BIGNUMBEROFPIECES)

    def test_creation_bad_pieces(self):
        with self.assertRaises(ValueError) as context:
            unhappy.Unhappy(BADNUMPIECES)
        self.assertTrue(context.exception)

    def test_creation_to_draw_default(self):
        x = unhappy.Unhappy()
        self.assertEqual(x.to_draw, 0)

    def test_confirm_clear_method(self):
        x = unhappy.Unhappy()
        x.to_draw = 1
        self.assertEqual(x.to_draw, 1)
        x.clear()
        self.assertEqual(x.to_draw, 0)

    def test_confirm_increment(self):
        x = unhappy.Unhappy()
        x.incr()
        x.incr()
        self.assertEqual(x.to_draw, 2)


if __name__ == '__main__':
    unittest.main()
