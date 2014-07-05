# unit tests for Mini-project 3 (simplified Yahtzee), by k., 07/04/2014

import unittest
from mini_project3 import score
from mini_project3 import expected_value
from mini_project3 import gen_all_holds
from mini_project3 import gen_all_sequences
from mini_project3 import strategy


class TestFourFunctions(unittest.TestCase):
    def setUp(self):
        pass
    def test_score(self):
        self.assertIs(type(score((2, 3, 3, 3, 4))), int)
        self.assertEqual(score((2, 3, 3, 3, 4)), 9)
        self.assertEqual(score((0, 0, 0, 0, 0)), 0)
        self.assertEqual(score((6, 6, 6, 6, 6)), 30)
        self.assertEqual(score((6, 5, 1, 5, 6)), 12)
        self.assertEqual(score((5, 4, 3, 2, 1)), 5)
        self.assertEqual(score((1, 1, 2, 2, 3)), 4)
        self.assertEqual(score((1, 1, 2, 2, 5)), 5)
        self.assertEqual(score((1, 1, 1, 1, 5)), 5)
        self.assertEqual(score((1, 2, 3, 4, 6)), 6)
    def test_expected(self):
        self.assertIs(type(expected_value((1, 2, 3, 4, 5), 6, 0)), float)
        self.assertAlmostEqual(expected_value((1, ), 6, 4), 7.53472222)
        self.assertEqual(expected_value((1, 2, 3, 4, 5), 6, 0), 5.0)
        self.assertEqual(expected_value((1, 3, 3, 6), 6, 1), 7.5)
        self.assertAlmostEqual(expected_value((1, 1, 2, 1), 6, 1), 4.3333333)
        self.assertEqual(expected_value((1, 1, 1, 1), 6, 1), 28 / 6.0)
        self.assertEqual(expected_value((2, 2, 2, 3), 6, 1), 38 / 6.0)
        # following items have incorrect number of dice, would trigger exception messages
        self.assertAlmostEqual(expected_value((1, 2,), 6, 4), 7.66898148)
        self.assertEqual(expected_value((1, 2, 3, 4, 5), 5, 1), 6.8)
        self.assertAlmostEqual(expected_value((), 6, 2), 5.0555556)
        self.assertAlmostEqual(expected_value((2, 1, 2), 6, 3), 6.9120370)
        self.assertAlmostEqual(expected_value((2, ), 6, 5), 8.8801440)
        self.assertAlmostEqual(expected_value((1, ), 6, 2), 5.0833333)
        self.assertAlmostEqual(expected_value((2, 1), 6, 3), 6.4722222)
        self.assertAlmostEqual(expected_value((2, 2), 6, 5), 9.2250514)
        self.assertAlmostEqual(expected_value((1, 2), 6, 4), 7.6689815)
    def test_all_sequences(self):
        self.assertIs(type(gen_all_holds((1, 2, 3, 4, 5))), set)
        in_it = gen_all_holds((1, 2, 3, 4, 5))
        for item in in_it:
            self.assertIs(type(item), tuple)
        # where values in the tuple hand happen to be distinct, the set of tuples returned
        # by gen_all_holds will correspond to all possible subsets of hand
        sequence = [(1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (2, 3, 4, 5, 6), (1, 3, 4, 5, 6)]
        for index, item in enumerate(sequence):
            gen_all_holds(item) == gen_all_sequences(sequence[index], 5)
        self.assertItemsEqual(gen_all_holds((4, 2)), [(), (4,), (2,), (4, 2)])
        self.assertItemsEqual(gen_all_holds((1, 2, 2)),
                              [(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)])
        self.assertItemsEqual(gen_all_holds((2, 1, 2)),
                              [(), (1,), (2,), (1, 2), (2, 1), (2, 2), (2, 1, 2)])
        self.assertItemsEqual(gen_all_holds((6, 2, 3)),
                              [(), (6,), (2,), (6, 2), (3,), (6, 3), (2, 3), (6, 2, 3)])
    def test_strategy(self):
        state = strategy((1,), 6)
        score, hand = state
        self.assertIs(type(score), float)
        self.assertIs(type(hand), tuple)
        self.assertIs(type(strategy((1,), 6)), tuple)
        self.assertEqual(strategy((1,), 6), (3.5, ()))
        self.assertEqual(strategy((1, 3, 5, 3, 3), 5), (10.24, (3, 3, 3)))
        self.assertEqual(strategy((3, 3, 3, 3), 4), (12.0, (3, 3, 3, 3)))
        self.assertEqual(strategy((3, 1, 4, 4, 4), 4), (14.0, (4, 4, 4)))
        self.assertEqual(strategy((1, 8, 4, 8), 8), (18.0, (8, 8)))
        self.assertEqual(strategy((3, 1, 1, 3, 2), 4), (8.53125, (3, 3)))
        self.assertEqual(strategy((6, 5), 6), (7.0, (6, )))
        self.assertEqual(strategy((1, 8, 8), 8), (17.0, (8, 8)))
                

# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
