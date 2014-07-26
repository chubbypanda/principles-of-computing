# unit tests for Mini-project 6 (Tic-Tac-Toe), by k., 07/25/2014

import unittest
from mini_project6 import TTTBoard
from mini_project6 import mm_move
from mini_project6 import DRAW, EMPTY, PLAYERO, PLAYERX


class TestFunction(unittest.TestCase):
    def setUp(self):
        pass
    def test_move_it(self):
        board = TTTBoard(3, False, [[PLAYERO, PLAYERX, PLAYERX], [PLAYERO, PLAYERX, PLAYERO], [PLAYERX, PLAYERO, PLAYERX]])
        self.assertIsInstance(board, TTTBoard)
        self.assertIs(type(mm_move(board, PLAYERX)), tuple)
        score, move = mm_move(board, PLAYERX)
        self.assertIs(type(score), int)
        self.assertIs(type(move), tuple)
        self.assertEqual(mm_move(board, PLAYERX), (1, (-1, -1)))
        board = TTTBoard(3, False, [[PLAYERO, PLAYERX, PLAYERX], [PLAYERX, PLAYERO, PLAYERO], [PLAYERO, PLAYERX, PLAYERX]])
        self.assertEqual(mm_move(board, DRAW), (0, (-1, -1)))
        board = TTTBoard(3, False, [[PLAYERO, PLAYERX, PLAYERX], [PLAYERO, PLAYERX, PLAYERO], [PLAYERO, PLAYERO, PLAYERX]])
        self.assertEqual(mm_move(board, PLAYERO), (-1, (-1, -1)))
    def test_won_it(self):
        board = TTTBoard(3, False, [[PLAYERX, PLAYERX, PLAYERO], [PLAYERO, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]])
        self.assertEqual(mm_move(board, PLAYERX), (1, (2, 1)))
        board = TTTBoard(2, False, [[EMPTY, EMPTY], [EMPTY, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERX), (1, (0, 0)))
    def test_draw(self):
        board = TTTBoard(3, False, [[EMPTY, EMPTY, PLAYERX], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERO), (0, (1, 1)))
        board = TTTBoard(3, False, [[PLAYERX, EMPTY, EMPTY], [PLAYERO, PLAYERO, EMPTY], [EMPTY, PLAYERX, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERX), (0, (1, 2)))
        board = TTTBoard(3, False, [[EMPTY, EMPTY, PLAYERX], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERO), (0, (1, 1)))  
    def test_lost_it(self):
        board = TTTBoard(3, False, [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]])
        self.assertEqual(mm_move(board, PLAYERO), (-1, (2, 1)))
        board = TTTBoard(3, False, [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]])
        self.assertEqual(mm_move(board, PLAYERO), (-1, (2, 1)))

              
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
