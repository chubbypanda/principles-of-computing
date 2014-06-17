# unit tests for Mini-project 0 (clone of 2048 game), by k., 06/16/2014

import unittest
from mini_project0 import merge
from mini_project0 import TwentyFortyEight

class TestFunction(unittest.TestCase):
    def test_merge(self):
        in0 = [0, 0, 0, 0]
        out0 = [0, 0, 0, 0]
        in1 = [2, 4, 8, 16]
        out1 = [2, 4, 8, 16]
        in2 = [0, 0, 0, 2]
        out2 = [2, 0, 0, 0]
        in3 = [2, 0, 2, 4]
        out3 = [4, 4, 0, 0]
        in4 = [0, 0, 2, 2]
        out4 = [4, 0, 0, 0]
        in5 = [2, 2, 0, 0]
        out5 = [4, 0, 0, 0]
        in6 = [2, 2, 2, 2]
        out6 = [4, 4, 0, 0]
        in7 = [4, 4, 4, 4]
        out7 = [8, 8, 0, 0]
        in8 = [8, 16, 16, 8]
        out8 = [8, 32, 8, 0]
        in9 = [0, 2, 1024, 1024]
        out9 = [2, 2048, 0, 0]
        in10 = [2]
        out10 = [2]
        assert (merge(in0)) == out0
        assert (merge(in1)) == out1
        assert (merge(in2)) == out2
        assert (merge(in3)) == out3
        assert (merge(in4)) == out4
        assert (merge(in5)) == out5
        assert (merge(in6)) == out6
        assert (merge(in7)) == out7
        assert (merge(in8)) == out8
        assert (merge(in9)) == out9
        assert (merge(in10)) == out10
        

class TestClass(unittest.TestCase):
    def setUp(self):
        self.array_move = TwentyFortyEight(4, 4)
        self.array_move.set_tile(0, 0, 0)
        self.array_move.set_tile(0, 1, 0)
        self.array_move.set_tile(0, 2, 0)
        self.array_move.set_tile(0, 3, 2)
        self.array_move.set_tile(1, 0, 0)
        self.array_move.set_tile(1, 1, 0)
        self.array_move.set_tile(1, 2, 2)
        self.array_move.set_tile(1, 3, 4)
        self.array_move.set_tile(2, 0, 0)
        self.array_move.set_tile(2, 1, 2)
        self.array_move.set_tile(2, 2, 8)
        self.array_move.set_tile(2, 3, 8)
        self.array_move.set_tile(3, 0, 2)
        self.array_move.set_tile(3, 1, 8)
        self.array_move.set_tile(3, 2, 8)
        self.array_move.set_tile(3, 3, 16)
    def test_create_array(self):
        array = TwentyFortyEight(4, 5)
        assert array.get_grid_height() == 4
        assert array.get_grid_width() == 5
    def test_array_reset(self):
        array = TwentyFortyEight(4, 4)
        for elem in xrange(array.get_grid_height()):
            for num in xrange(array.get_grid_width()):
                assert array.get_tile(elem, num) == 0
    def test_reseted_array(self):
        array = TwentyFortyEight(8, 8)
        self.test_array_reset()
        array.reset()
        self.test_array_reset()
        array.set_tile(3, 3, 2048)
        array.reset()
        self.test_array_reset()
    def test_reading_from_array(self):
        array = TwentyFortyEight(4, 4)
        self.assertEqual(array.get_tile(1, 1), 0)
    def test_writing_into_array(self):
        array = TwentyFortyEight(4, 4)
        array.set_tile(3, 3, 32)
        assert array.get_tile(3, 3) == 32
    def test_new_tile(self):
        array = TwentyFortyEight(10, 10)
        found = 0
        array.new_tile()
        for elem in xrange(array.get_grid_height()):
            for num in xrange(array.get_grid_width()):
                if array.get_tile(elem, num) in (2, 4):
                    found += 1
        self.assertEqual(found, 1)
    def test_move_down(self):
        self.array_move.move(2)
        self.assertEqual(self.array_move.get_tile(0, 3), 2)
        self.assertEqual(self.array_move.get_tile(1, 3), 4)
        self.assertEqual(self.array_move.get_tile(2, 2), 2)
        self.assertEqual(self.array_move.get_tile(2, 3), 8)
        self.assertEqual(self.array_move.get_tile(3, 0), 2)
        self.assertEqual(self.array_move.get_tile(3, 1), 8)
        self.assertEqual(self.array_move.get_tile(3, 2), 16)
        self.assertEqual(self.array_move.get_tile(3, 3), 16)
    def test_move_up(self):
        self.array_move.move(1)
        self.assertEqual(self.array_move.get_tile(0, 0), 2)
        self.assertEqual(self.array_move.get_tile(0, 1), 2)
        self.assertEqual(self.array_move.get_tile(0, 2), 2)
        self.assertEqual(self.array_move.get_tile(0, 3), 2)
        self.assertEqual(self.array_move.get_tile(1, 1), 8)
        self.assertEqual(self.array_move.get_tile(1, 2), 16)
        self.assertEqual(self.array_move.get_tile(1, 3), 4)
        self.assertEqual(self.array_move.get_tile(2, 3), 8)
        self.assertEqual(self.array_move.get_tile(3, 3), 16)
    def test_move_right(self):
        self.array_move.move(4)
        self.assertEqual(self.array_move.get_tile(0, 3), 2)
        self.assertEqual(self.array_move.get_tile(1, 2), 2)
        self.assertEqual(self.array_move.get_tile(1, 3), 4)
        self.assertEqual(self.array_move.get_tile(2, 2), 2)
        self.assertEqual(self.array_move.get_tile(2, 3), 16)
        self.assertEqual(self.array_move.get_tile(3, 1), 2)
        self.assertEqual(self.array_move.get_tile(3, 2), 16)
        self.assertEqual(self.array_move.get_tile(3, 3), 16)
    def test_move_left(self):
        self.array_move.move(3)
        self.assertEqual(self.array_move.get_tile(0, 0), 2)
        self.assertEqual(self.array_move.get_tile(1, 0), 2)
        self.assertEqual(self.array_move.get_tile(1, 1), 4)
        self.assertEqual(self.array_move.get_tile(2, 0), 2)
        self.assertEqual(self.array_move.get_tile(2, 1), 16)
        self.assertEqual(self.array_move.get_tile(3, 0), 2)
        self.assertEqual(self.array_move.get_tile(3, 1), 16)
        self.assertEqual(self.array_move.get_tile(3, 2), 16)
        

# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
