# unit tests for Practice Activity 3 (Analyzing a simple dice game), by k., 07/04/2014

import unittest
from practice_activity3 import max_repeats
from practice_activity3 import compute_expected_value


class TestFunctions(unittest.TestCase):
    def test_set_state(self):
        self.assertEqual(max_repeats((3, 3, 3)), 3)
        self.assertEqual(max_repeats((6, 6, 2)), 2)
        self.assertEqual(max_repeats((1, )), 1)
        self.assertEqual(max_repeats((3, 2, 1)), 1)
        self.assertEqual(max_repeats((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                      14, 15, 16, 17, 18, 19, 20, 21)), 1)
        self.assertEqual(max_repeats((21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                                      10, 9, 8, 7, 6, 5, 4, 3, 2, 1)), 1)
        self.assertEqual(max_repeats((9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                      9, 9, 9, 9, 9, 9, 9, 9, 9, 9)), 20)
        self.assertEqual(max_repeats((1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)), 6)
        self.assertEqual(max_repeats((1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)), 4)
        self.assertEqual(max_repeats((1, 2, 2, 2, 2, 2, 2, 1)), 6)
        self.assertEqual(max_repeats((2, 2, 2, 2, 1, 2, 2, 2, 2)), 8)
        self.assertEqual(max_repeats((1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4)), 4)
    def test_check_result(self):
        self.assertIs(type(compute_expected_value()), float)
        self.assertAlmostEqual(compute_expected_value(), 9.7222222)
        

# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
