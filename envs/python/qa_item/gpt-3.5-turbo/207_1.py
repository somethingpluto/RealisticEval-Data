from typing import List

def min_changes_to_symmetric(matrix: List[List]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    
    changes = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                changes += 1
                
    return changes
import unittest


class Tester(unittest.TestCase):
    def test_already_symmetric_matrix(self):
        matrix = [
            ['a', 'b', 'c'],
            ['b', 'e', 'f'],
            ['c', 'f', 'i']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 0)

    def test_one_change_needed(self):
        matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['c', 'h', 'i']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 2)

    def test_all_different_elements(self):
        matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 3)

    def test_large_symmetric_matrix(self):
        matrix = [
            ['a', 'b', 'c', 'd'],
            ['b', 'e', 'f', 'g'],
            ['c', 'f', 'h', 'i'],
            ['d', 'g', 'i', 'j']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 0)

    def test_multiple_changes_needed(self):
        matrix = [
            ['a', 'x', 'c', 'd'],
            ['y', 'e', 'f', 'g'],
            ['z', 'h', 'i', 'j'],
            ['d', 'g', 'k', 'l']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 4)

if __name__ == '__main__':
    unittest.main()