# unit tests for Mini-project 2 (Tic-Tac-Toe), by k., 06/27/2014

import unittest
from mini_project2 import TTTBoard
from mini_project2 import switch_player
from mini_project2 import play_game
from mini_project2 import get_best_move
from mini_project2 import mc_trial
from mini_project2 import mc_update_scores
from mini_project2 import mc_move


class TestFunction(unittest.TestCase):
    def setUp(self):
        pass 
    def test_best_move(self):
        my_board = TTTBoard(3, board = [[2, 3, 2], [1, 1, 1], [1, 2, 3]])
        scores = [[3.0, 5.0, -1.0], [3.0, 2.0, -8.0], [4.0, -2.0, 2.0]]
        print my_board
        print "scores:", scores
        self.assertEqual(get_best_move(my_board, scores), (2, 0))
        self.assertIs(type(get_best_move(my_board, scores)), tuple)
    def test_two_best_moves(self):
        my_board = TTTBoard(3, board = [[1, 1, 2], [1, 3, 1], [2, 3, 1]])
        scores = [[0.0, 2.0, 1.0], [0.0, 2.0, -1.0], [1.0, -2.0, 2.0]]
        print '\n', my_board
        print "scores:", scores
        possible_squares = ((0, 1), (2, 2))
        assert get_best_move(my_board, scores) in possible_squares
    def test_three_best_moves(self):
        my_board = TTTBoard(3, board = [[1, 3, 2], [1, 3, 1], [2, 2, 1]])
        scores = [[2.0, 2.0, 2.0], [2.0, 2.0, -1.0], [2.0, -2.0, 2.0]]
        print '\n', my_board
        print "scores:", scores
        possible_squares = ((0, 0), (1, 0), (2, 2))
        assert get_best_move(my_board, scores) in possible_squares
    def test_trial_before_after(self):
        # dimension size 3
        initial_board = TTTBoard(3)
        my_board = initial_board.clone()
        self.assertEqual(my_board.check_win(), None)
        mc_trial(my_board, 2)
        self.assertNotEqual(my_board.check_win(), None)
            # check that function does not return anything
        self.assertEqual(mc_trial(my_board, 2), None)
        # dimension size 40
        initial_board = TTTBoard(40)
        my_board = initial_board.clone()
        self.assertEqual(my_board.check_win(), None)
        mc_trial(my_board, 3)
        self.assertNotEqual(my_board.check_win(), None)
            # check that function does not return anything
        self.assertEqual(mc_trial(my_board, 2), None)
    def test_zscores_updated(self):
        # DRAW (no winners), for both players played
        my_board = TTTBoard(3, board = [[1, 3, 2], [1, 3, 1], [2, 2, 1]])
        scores = [[2.0, 2.0, 2.0], [2.0, 2.0, -1.0], [2.0, -2.0, 2.0]]
        mc_update_scores(scores, my_board, 3)
            # check that function does not return anything
        self.assertEqual(mc_update_scores(scores, my_board, 2), None)
        self.assertEqual(scores, scores)
        mc_update_scores(scores, my_board, 2)
        self.assertEqual(scores, scores)
        my_board = TTTBoard(3, board = [[2, 3, 2], [3, 3, 2], [3, 2, 3]])
        scores = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        mc_update_scores(scores, my_board, 3)
        self.assertEqual(scores, scores)
        mc_update_scores(scores, my_board, 2)
        self.assertEqual(scores, scores)
        # PLAYERO wins
        my_board = TTTBoard(3, board = [[1, 3, 2], [1, 3, 1], [2, 3, 1]])
        scores = [[2.0, 2.0, 2.0], [2.0, 2.0, -1.0], [2.0, -2.0, 2.0]]
        mc_update_scores(scores, my_board, 3)
        self.assertEqual(scores, [[2.0, 3.0, 1.0], [2.0, 3.0, -1.0], [1.0, -1.0, 2.0]])
            # check that function does not return anything
        self.assertEqual(mc_update_scores(scores, my_board, 3), None)
        my_board = TTTBoard(3, board = [[1, 3, 2], [1, 3, 1], [2, 3, 1]])
        scores = [[2.0, 2.0, 2.0], [2.0, 2.0, -1.0], [2.0, -2.0, 2.0]]
        mc_update_scores(scores, my_board, 2)
        self.assertEqual(scores, [[2.0, 3.0, 1.0], [2.0, 3.0, -1.0], [1.0, -1.0, 2.0]])
            # check that function does not return anything
        self.assertEqual(mc_update_scores(scores, my_board, 2), None)
        # PLAYERX wins
        my_board = TTTBoard(3, board = [[2, 3, 2], [3, 3, 2], [3, 2, 2]])
        scores = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        mc_update_scores(scores, my_board, 2)
        self.assertEqual(scores, [[1.0, -1.0, 1.0], [-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0]])
            # check that function does not return anything
        self.assertEqual(mc_update_scores(scores, my_board, 2), None)
        my_board = TTTBoard(3, board = [[2, 3, 2], [3, 3, 2], [3, 2, 2]])
        scores = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        mc_update_scores(scores, my_board, 3)
        self.assertEqual(scores, [[1.0, -1.0, 1.0], [-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0]])
            # check that function does not return anything
        self.assertEqual(mc_update_scores(scores, my_board, 3), None)
    def test_move_it(self):
        my_board = TTTBoard(3, board = [[1, 3, 2], [1, 3, 1], [2, 3, 1]])
        possible_squares = ((0, 0), (1, 0), (1, 2), (2, 2))
        assert mc_move(my_board, 3, 100) in possible_squares
        self.assertIs(type(mc_move(my_board, 3, 100)), tuple)
        # one empty square left
        my_board = TTTBoard(3, board = [[3, 3, 2], [2, 3, 2], [2, 3, 1]])
        self.assertEqual(mc_move(my_board, 3, 100), (2, 2))


# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
