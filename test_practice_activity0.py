# unit tests for Practice Activity 0 (Solitaire Mancala), by k., 06/19/2014

import unittest
from practice_activity0 import SolitaireMancala


class TestClass(unittest.TestCase):
    def setUp(self):
        self.state = SolitaireMancala()
        # the only winner configurations for six houses board
        self.win = [[0, 0, 0, 0, 2, 4, 6], 
                    [0, 0, 0, 2, 4, 0, 0], 
                    [0, 0, 1, 1, 3, 5, 0], 
                    [0, 0, 1, 3, 0, 0, 0], 
                    [0, 0, 1, 3, 2, 4, 6], 
                    [0, 0, 2, 0, 0, 0, 0], 
                    [0, 0, 2, 0, 2, 4, 6], 
                    [0, 0, 2, 2, 4, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0], 
                    [0, 1, 0, 0, 2, 4, 6], 
                    [0, 1, 0, 2, 4, 0, 0], 
                    [0, 1, 1, 1, 3, 5, 0], 
                    [0, 1, 1, 3, 0, 0, 0], 
                    [0, 1, 1, 3, 2, 4, 6], 
                    [0, 1, 2, 0, 0, 0, 0], 
                    [0, 1, 2, 0, 2, 4, 6], 
                    [0, 1, 2, 2, 4, 0, 0]]

    def test_init_state(self):
        self.assertEqual(str(self.state), str([0]))
    def test_set_state(self):
        self.state.set_board([0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(str(self.state), str([0, 0, 0, 0, 0, 0, 0]))
        self.state.set_board([0, 0, 1, 1, 3, 5])
        self.assertEqual(str(self.state), str([5, 3, 1, 1, 0, 0]))
    def test_get_seeds(self):
        self.state.set_board([0, 0, 1, 1, 3, 5])
        self.assertEqual(self.state.get_num_seeds(0), 0)
        self.assertEqual(self.state.get_num_seeds(1), 0)
        self.assertEqual(self.state.get_num_seeds(2), 1)
        self.assertEqual(self.state.get_num_seeds(3), 1)
        self.assertEqual(self.state.get_num_seeds(4), 3)
        self.assertEqual(self.state.get_num_seeds(5), 5)
        self.assertNotEqual(self.state.get_num_seeds(5), 6)
    def test_legal_moves(self):
        self.state.set_board([0, 1, 2, 3, 4, 5, 6])
        for house in [1, 2, 3, 4, 5, 6]:
            self.assertTrue(self.state.is_legal_move(house))
        self.state.set_board([0, 2, 3, 4, 5, 6, 3])
        for house in [0, 2, 3, 4, 5, 6, 3]:
            self.assertFalse(self.state.is_legal_move(house))
    def test_i_like_to_move_it(self):
        self.state.set_board([0, 1, 2, 0, 2, 4, 6])
        self.state.apply_move(1)
        self.assertEqual(str(self.state), str([6, 4, 2, 0, 2, 0, 1]))
        self.state.set_board([0, 1, 2, 0, 2, 4, 6])
        self.state.apply_move(2)
        self.assertEqual(str(self.state), str([6, 4, 2, 0, 0, 2, 1]))
        self.state.set_board([0, 1, 2, 0, 2, 4, 6])
        self.state.apply_move(6)
        self.assertEqual(str(self.state), str([0, 5, 3, 1, 3, 2, 1]))
    def test_i_wanna_move_it_all(self):
        board = [1, 1, 2, 2, 4, 0]
        self.state.set_board(board)
        legal_sequence = [1, 2, 1, 4, 1, 3, 1, 2, 1]
        for game in xrange(len(board)):
            self.assertEqual(self.state.choose_move(), legal_sequence[game])
            self.state.apply_move(legal_sequence[game])
    def test_providing_moves(self):
        self.state.set_board([0, 1, 1, 3, 2, 4, 6])
        self.assertEqual(self.state.choose_move(), 1)
        self.state.set_board([1, 0, 1, 3, 2, 4, 6])
        self.assertEqual(self.state.choose_move(), 3)
        self.state.set_board([2, 1, 2, 0, 2, 4, 6])
        self.assertEqual(self.state.choose_move(), 1)
        self.state.set_board([3, 0, 2, 0, 2, 4, 6])
        self.assertEqual(self.state.choose_move(), 2)
    def test_moves_and_applies(self):
        self.state.set_board([0, 0, 1, 1, 3, 5])
        self.assertEqual(self.state.choose_move(), 5)
        self.state.apply_move(5)
        self.assertEqual(str(self.state), str([0, 4, 2, 2, 1, 1]))
        self.state.set_board([0, 0, 1, 1, 3, 4])
        self.assertEqual(self.state.choose_move(), 0)
    def test_won(self):
        for game in xrange(len(self.win)):
            self.state.set_board(self.win[game])
            self.assertFalse(self.state.is_game_won())
        self.state.set_board([15, 0, 0, 0, 0, 0, 0])
        self.assertTrue(self.state.is_game_won())
    def test_move_it(self):
        for game in xrange(len(self.win)):
            self.state.set_board(self.win[game])
            self.state.plan_moves()
            self.assertTrue(self.state.is_game_won())
    def test_fail_it(self):
        self.state.set_board([0, 1, 2, 2, 4, 0, 1])
        self.state.plan_moves()
        self.assertFalse(self.state.is_game_won())
        self.state.set_board([0, 0, 1])
        self.assertFalse(self.state.is_legal_move(1))
        self.assertFalse(self.state.is_legal_move(2))
        self.state.plan_moves()
        self.assertFalse(self.state.is_game_won())


# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
