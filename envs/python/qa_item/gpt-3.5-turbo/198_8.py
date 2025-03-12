from typing import List

def find_max_difference(l: List[int]) -> int:
    if not l:
        return 0
    
    min_element = l[0]
    max_difference = 0
    
    for i in range(1, len(l)):
        if l[i] < min_element:
            min_element = l[i]
        else:
            max_difference = max(max_difference, l[i] - min_element)
    
    return max_difference
import unittest


class Tester(unittest.TestCase):

    def test_general_case(self):
        l = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(find_max_difference(l), 8)  # Maximum difference is 10 - 2 = 8

    def test_decreasing_sequence(self):
        l = [10, 9, 8, 7, 6, 5]
        self.assertEqual(find_max_difference(l), 0)  # Maximum difference should be 0

    def test_all_elements_same(self):
        l = [5, 5, 5, 5, 5]
        self.assertEqual(find_max_difference(l), 0)  # Maximum difference is 5 - 5 = 0

    def test_only_two_elements(self):
        l = [3, 8]
        self.assertEqual(find_max_difference(l), 5)  # Maximum difference is 8 - 3 = 5

    def test_single_element(self):
        l = [4]
        self.assertEqual(find_max_difference(l), 0)  # Only one element, no difference to calculate

if __name__ == '__main__':
    unittest.main()