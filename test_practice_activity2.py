# unit tests for Practice Activity 2 (simplified Nim, Monte Carlo solver), by k., 07/07/2014

import unittest
from practice_activity2 import evaluate_position


class TestFunction(unittest.TestCase):
    def test_set_state(self):
        self.assertIs(type(evaluate_position(10)), int)
        # for 10000 trials determining the optimal move starts to be reliable
        # between 12 to 15 items
        self.assertEqual(evaluate_position(13), 1)
        self.assertEqual(evaluate_position(10), 2)
        self.assertEqual(evaluate_position(9), 1)
        self.assertEqual(evaluate_position(7), 3)


# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
