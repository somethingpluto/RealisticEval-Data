def create_matrix(rows: int, columns: int, initial_value: any) -> list:
    """Creates a matrix with the specified number of rows and columns,
    filled with the given initial value.

    Args:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.
        initial_value (any): The value to fill the matrix with.
                             It can be of any type (number, string, object, etc.).

    Returns:
        list: A two-dimensional list (matrix) filled with the initial value.
    """
    return [[initial_value for _ in range(columns)] for _ in range(rows)]
import unittest


class TestCreateMatrix(unittest.TestCase):

    def test_create_2x2_matrix_filled_with_zeros(self):
        result = create_matrix(2, 2, 0)
        self.assertEqual(result, [[0, 0], [0, 0]])

    def test_create_3x3_matrix_filled_with_ones(self):
        result = create_matrix(3, 3, 1)
        self.assertEqual(result, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    def test_create_4x5_matrix_filled_with_string(self):
        result = create_matrix(4, 5, 'test')
        self.assertEqual(result, [['test'] * 5 for _ in range(4)])

    def test_create_0x0_matrix(self):
        result = create_matrix(0, 0, None)
        self.assertEqual(result, [])

    def test_create_1x1_matrix_with_boolean(self):
        result = create_matrix(1, 1, True)
        self.assertEqual(result, [[True]])

    def test_create_5x5_matrix_filled_with_negative_numbers(self):
        result = create_matrix(5, 5, -1)
        self.assertEqual(result, [[-1] * 5 for _ in range(5)])

if __name__ == '__main__':
    unittest.main()