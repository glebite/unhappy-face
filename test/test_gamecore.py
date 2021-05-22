import unittest
import gamecore


class Testing(unittest.TestCase):
    def test_creation(self):
        x = gamecore.GameCore('nonce')
        self.assertNotEqual(x, None)

    def test_check_stats(self):
        rc = True
        x = gamecore.GameCore('nonce')
        for key in x.stats.keys():
            if x.stats[key] != 0:
                rc = False
        self.assertTrue(rc)

    def test_incr_bad_stat(self):
        x = gamecore.GameCore('nonce')
        with self.assertRaises(ValueError) as context:
            x.incr_stat('unknown')
        self.assertTrue(context.exception)

    def test_incr_good_stat(self):
        x = gamecore.GameCore('nonce')
        x.incr_stat('win')
        self.assertEqual(x.stats['win'], 1)

    def test_clear_stats(self):
        rc = True
        x = gamecore.GameCore('nonce')
        x.incr_stat('win')
        x.clear_stats()
        for key in x.stats.keys():
            if x.stats[key] != 0:
                rc = False
        self.assertTrue(rc)


if __name__ == '__main__':
    unittest.main()
