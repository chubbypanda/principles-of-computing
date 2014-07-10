# unit tests for Practice Activity 4 (Working with Distance Fields), by k., 07/10/2014

import unittest
from practice_activity4 import manhattan_distance
from practice_activity4 import create_distance_field
from practice_activity4 import GRID_WIDTH
from practice_activity4 import GRID_HEIGHT

class TestFunctions(unittest.TestCase):
    def test_arbitrary_distances(self):
        self.assertIs(type(manhattan_distance(1, 2, 3, 4)), int)
        self.assertEqual(manhattan_distance(1, 1, 1, 1), 0)
        self.assertEqual(manhattan_distance(0, 0, 1, 1), 2)
        self.assertEqual(manhattan_distance(0, 4, 8, 4), 8)
        self.assertEqual(manhattan_distance(4, 0, 4, 8), 8)
        self.assertEqual(manhattan_distance(0, 4, 4, 0), 8)
        self.assertEqual(manhattan_distance(4, 0, 8, 4), 8)
        self.assertEqual(manhattan_distance(8, 4, 4, 8), 8)
        self.assertEqual(manhattan_distance(4, 8, 0, 4), 8)
        self.assertEqual(manhattan_distance(0, 4, 4, 4), 4)
        self.assertEqual(manhattan_distance(4, 0, 4, 4), 4)
        self.assertEqual(manhattan_distance(8, 4, 4, 4), 4)
        self.assertEqual(manhattan_distance(4, 8, 4, 4), 4)
        self.assertEqual(manhattan_distance(0, 0, 8, 8), 16)
    def test_entity_distances(self):
        self.assertIs(type(create_distance_field([[4, 0],[2, 5]])), list)
        out1 = [[4, 5, 5, 4, 3, 2, 3, 4],
                [3, 4, 4, 3, 2, 1, 2, 3],
                [2, 3, 3, 2, 1, 0, 1, 2],
                [1, 2, 3, 3, 2, 1, 2, 3],
                [0, 1, 2, 3, 3, 2, 3, 4],
                [1, 2, 3, 4, 4, 3, 4, 5]]
        self.assertEqual(create_distance_field([[4, 0],[2, 5]]), out1)
        out2 = [[4, 5, 5, 4, 3, 2, 3, 4],
                [3, 4, 4, 3, 2, 1, 2, 3],
                [2, 3, 3, 2, 1, 0, 1, 2],
                [1, 2, 3, 2, 1, 1, 2, 3],
                [0, 1, 2, 1, 0, 1, 2, 3],
                [1, 2, 3, 2, 1, 2, 3, 4]]
        self.assertEqual(create_distance_field([[4, 0], [2, 5], [4, 4]]), out2)
        # placing entity on every other cell shall result in alternated 0, 1 distances
        in4 = [[0, 0], [0, 2], [0, 4], [0, 6],
               [1, 0], [1, 2], [1, 4], [1, 6],
               [2, 0], [2, 2], [2, 4], [2, 6],
               [3, 0], [3, 2], [3, 4], [3, 6],
               [4, 0], [4, 2], [4, 4], [4, 6],
               [5, 0], [5, 2], [5, 4], [5, 6]]
        out4 = [[0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1]]
        self.assertEqual(create_distance_field(in4), out4)
        # placing entity on every single cell shall result in 0 distances everywhere
        in3 = [[x, y] for x in range(GRID_HEIGHT) for y in range(GRID_WIDTH)]
        out3 = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]
        self.assertEqual(create_distance_field(in3), out3)
    

# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
