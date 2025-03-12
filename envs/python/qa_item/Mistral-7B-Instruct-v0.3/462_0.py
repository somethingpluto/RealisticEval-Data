from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(m)]
    result = []

    x, y, d = 0, 0, 0
    while True:
        visited[x][y] = True
        result.append(matrix[x][y])

        next_x, next_y = x + direction[d][0], y + direction[d][1]

        if (next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or matrix[next_x][next_y] is None or visited[next_x][next_y]):
            d = (d + 1) % 4
            x, y = x + direction[d][0], y + direction[d][1]
        else:
            x, y = next_x, next_y

        if x == m - 1 and y == n - 1:
            break

    return result
import unittest


class TestSpiralOrder(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(spiral_order([]), [])

    def test_single_row_matrix(self):
        self.assertEqual(spiral_order([[1, 2, 3]]), [1, 2, 3])

    def test_single_column_matrix(self):
        self.assertEqual(spiral_order([[1], [2], [3]]), [1, 2, 3])

    def test_square_matrix(self):
        self.assertEqual(spiral_order([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_rectangle_matrix(self):
        self.assertEqual(spiral_order([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
if __name__ == '__main__':
    unittest.main()