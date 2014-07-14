# unit tests for Mini-project 4 (Zombie Apocalypse), by k., 07/11/2014

import unittest
from mini_project4 import Queue
from mini_project4 import Grid
from mini_project4 import Zombie


class TestClassZombine(unittest.TestCase):
    def setUp(self):
        pass
    def test_states(self):
        state = Zombie(8, 6)
        state.clear()
        self.assertIs(type(state.num_zombies()), int)
        self.assertEqual(state.num_zombies(), 0)
        self.assertIs(type(state.num_humans()), int)
        self.assertEqual(state.num_humans(), 0)
        state.add_zombie(4, 4)
        self.assertEqual(state.num_zombies(), 1)
        state.add_human(4, 4)
        self.assertEqual(state.num_zombies(), 1)
        state.clear()
        self.assertEqual(state.num_zombies(), 0)
        self.assertEqual(state.num_humans(), 0)
        for dummy_row in range(state._grid_height):
            for dummy_col in range(state._grid_width):
                self.assertTrue(state.is_empty(dummy_row, dummy_col))
        state.set_full(0, 0)
        self.assertFalse(state.is_empty(0, 0))
        state.add_human(0, 1)
        state.add_human(1, 1)
        state.add_human(2, 1)
        state.add_human(3, 1)
        self.assertEqual(state.num_humans(), 4)
        state.clear()
        state = Zombie(10, 10)
        state.add_zombie(2, 3)
        self.assertTrue(state.zombies())
        state.add_human(3, 2)
        self.assertTrue(state.humans())
    def test_returns_in_order(self):
        state = Zombie(8, 8)
        state.add_human(1, 1)
        state.add_human(2, 2)
        state.add_human(3, 3)
        iteration = 1
        for each in state.humans():
            self.assertEqual(each, (iteration, iteration))
            iteration += 1
        state.clear()
        state = Zombie(4, 4)
        state.add_zombie(1, 1)
        state.add_zombie(2, 2)
        state.add_zombie(3, 3)
        iteration = 1
        for each in state.zombies():
            self.assertEqual(each, (iteration, iteration))
            iteration += 1
    def test_distances(self):
        state = Zombie(2, 3, zombie_list = [(0, 0)])
        self.assertEqual(state.compute_distance_field('zombie'), [[0, 1, 2], [1, 2, 3]])
        state = Zombie(2, 3, human_list = [(1, 2)])
        self.assertEqual(state.compute_distance_field('human'), [[3, 2, 1], [2, 1, 0]])
        state = Zombie(3, 3, [], [], [(2, 2)])
        self.assertEqual(state.compute_distance_field('human'), [[4, 3, 2], [3, 2, 1], [2, 1, 0]])
        state = Zombie(3, 3, [], [(1, 1)], [])
        self.assertEqual(state.compute_distance_field('zombie'), [[2, 1, 2], [1, 0, 1], [2, 1, 2]])
        state = Zombie(3, 3, obstacle_list = [(0, 1), (1, 1)], zombie_list = [(1, 2)])
        self.assertEqual(state.compute_distance_field('zombie'), [[5, 9, 1], [4, 9, 0], [3, 2, 1]])
        state = Zombie(3, 3, obstacle_list=[(1, 1), (2, 1)], zombie_list = [(2, 2)], human_list = [(0, 1)])
        self.assertEqual(state.compute_distance_field('human'), [[1, 0, 1], [2, 9, 2], [3, 9, 3]])
        obstacle_list = [(4, 15), (5, 15), (6, 15), (7, 15),
                         (8, 15), (9, 15), (10, 15), (11, 15),
                         (12, 15), (13, 15), (14, 15), (15, 10),
                         (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)]
        entity_list = [(7, 12), (12, 12)]
        expected_distance = [[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                             [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                             [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
                             [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                             [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 5, 600, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
                             [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                             [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                             [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 600, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
                             [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
                             [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
                             [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
                             [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                             [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 600, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                             [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                             [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                             [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 600, 600, 600, 600, 600, 600, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
                             [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
                             [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
                             [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                             [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
        state = Zombie(20, 30, obstacle_list, entity_list)
        self.assertEqual(state.compute_distance_field('zombie'), expected_distance)
        state = Zombie(20, 30, obstacle_list, [], entity_list)
        self.assertEqual(state.compute_distance_field('human'), expected_distance)
    def test_moving(self):
        state = Zombie(3, 3, obstacle_list = [(1, 1), (2, 1)], zombie_list = [(2, 2)], human_list = [(0, 1)])
        state.move_humans(state.compute_distance_field('zombie'))
        self.assertEqual(state._human_list, [(1, 0)])
        state.move_humans(state.compute_distance_field('zombie'))
        self.assertEqual(state._human_list, [(2, 0)])
        state.move_humans(state.compute_distance_field('zombie'))
        self.assertEqual(state._human_list, [(2, 0)])

                      
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
