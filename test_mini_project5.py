# unit tests for Mini-project 5 (Word Wrangler), by k., 07/18/2014

import unittest
from mini_project5 import remove_duplicates
from mini_project5 import intersect
from mini_project5 import merge
from mini_project5 import merge_sort
from mini_project5 import gen_all_strings


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass
    def test_deduplication(self):
        self.assertIs(type(remove_duplicates([1])), list)
        in1 = [1, 1, 1, 1, 2, 3, 5, 7, 99]
        out1 = [1, 2, 3, 5, 7, 99]
        self.assertEqual(remove_duplicates(in1), out1)
        in2 = ['aa', 'aa', 'ab', 'baf', 'naf', 'kool', 'q', 'q', 'q', 'q', 'zet', 'zet']
        out2 = ['aa', 'ab', 'baf', 'naf', 'kool', 'q', 'zet']
        self.assertEqual(remove_duplicates(in2), out2)
        in3 = []
        out3 = []
        self.assertEqual(remove_duplicates(in3), out3)
        in4 = [6]
        out4 = [6]
        self.assertEqual(remove_duplicates(in4), out4)
        in_out5 = [4, 5, 6, 9, 15, 22]
        self.assertEqual(remove_duplicates(in_out5), in_out5)
    def test_intersection(self):
        self.assertIs(type(intersect([1], [2])), list)
        in1a = [1, 3, 5, 7, 99]
        in1b = [1, 2, 4, 6, 8, 99]
        out1 = [1, 99]
        self.assertEqual(intersect(in1a, in1b), out1)
        in2a = [1, 3, 5, 7, 9, 10]
        in2b = [9, 10, 11, 99]
        out2 = [9, 10]
        self.assertEqual(intersect(in2a, in2b), out2)
        in3a = ['a', 'c', 'd', 'e', 'f', 'z']
        in3b = ['b', 'c', 'd', 'e', 'f', 'x']
        out3 = ['c', 'd', 'e', 'f']
        self.assertEqual(intersect(in3a, in3b), out3)
        in4 = [1, 2, 3]
        self.assertEqual(intersect(in4, in4), in4)
        in5a = [1, 2, 3]
        in5b = [5, 6, 7, 8, 9 , 10]
        self.assertEqual(intersect(in5a, in5b), [])
        self.assertEqual(intersect([], []), [])
    def test_merged(self):
        self.assertIs(type(merge([1], [2])), list)
        in1a = [1, 3, 5, 7, 99]
        in1b = [1, 2, 4, 6, 8, 99]
        out1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 99, 99]
        self.assertEqual(merge(in1a, in1b), out1)
        in2a = [1, 1, 1, 1]
        in2b = [2, 2, 2, 2]
        out2 = [1, 1, 1, 1, 2, 2, 2, 2]
        self.assertEqual(merge(in2a, in2b), out2)
        in3a = [2, 3, 4, 5, 6]
        in3b = [1, 10]
        out3 = [1, 2, 3, 4, 5, 6, 10]
        self.assertEqual(merge(in3a, in3b), out3)
        in3a = [2, 3, 4, 5, 6]
        in3b = [1, 10]
        self.assertEqual(merge(in3b, in3a), out3)
        in4a = [2, 4, 6, 8, 10]
        in4b = [2, 4, 6, 8, 10]
        out4 = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]
        self.assertEqual(merge(in4a, in4b), out4)
        in5a = ['people', 'welcoming', 'zombies']
        in5b = ['now']
        out5 = ['now', 'people', 'welcoming', 'zombies']
        self.assertEqual(merge(in5a, in5b), out5)
        in6a = ['people', 'welcoming', 'zombies']
        in6b = []
        out6 = ['people', 'welcoming', 'zombies']
        self.assertEqual(merge(in6a, in6b), out6)
        self.assertEqual(merge(in6b, in6a), out6)
        in7a = [1, 2, 3]
        in7b = [4, 5, 6]
        out7 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(merge(in7a, in7b), out7)
    def test_merge_sorted(self):
        self.assertIs(type(merge_sort([1])), list)
        in1 = []
        out1 = []
        self.assertEqual(merge_sort(in1), out1)
        in2 = [1]
        out2 = [1]
        self.assertEqual(merge_sort(in2), out2)
        in3 = [999, 400, 323, 109, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        out3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 109, 323, 400, 999]
        self.assertEqual(merge_sort(in3), out3)
        in4 = [1, 2, 1, 2, 1, 2]
        out4 = [1, 1, 1, 2, 2, 2]
        self.assertEqual(merge_sort(in4), out4)
        in5 = ['zac', 'hqsadsdao', 'agf', 'wefg', 'czz', 'urtereq', 'hrewqewrkihz']
        out5 = ['agf', 'czz', 'hqsadsdao', 'hrewqewrkihz', 'urtereq', 'wefg', 'zac']
        self.assertEqual(merge_sort(in5), out5)
        in6 = [6, 4]
        out6 = [4, 6]
        self.assertEqual(merge_sort(in6), out6)
    def test_possibilities(self):
        self.assertIs(type(gen_all_strings('')), list)
        self.assertEqual(gen_all_strings(''), [''])
        out1 = ['', 'a']    
        self.assertEqual(gen_all_strings('a'), out1)
        out2 = ['', 'b', 'a', 'ab', 'ba']    
        self.assertEqual(gen_all_strings('ab'), out2)
        out3 = ['', 'b', 'a', 'ab', 'ba', 'a', 'ab', 'ba', 'aa', 'aa',
               'aab', 'aab', 'aba', 'aba', 'baa', 'baa']    
        self.assertEqual(gen_all_strings('aab'), out3)
        out4 = ['', '1', '2', '21', '12']
        self.assertEqual(gen_all_strings('21'), out4)

                     
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
