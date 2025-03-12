from typing import List

def squared_euclidean_distance(vec1: List[int], vec2: List[int]) -> int:
    """
    compute the squared Euclidean distance between two vectors.

    Args:
        vec1 (List[int]): First vector.
        vec2 (List[int]): Second vector.

    Returns:
        int: Euclidean distance between vec1 and vec2.
    """
    distance = sum((x - y) ** 2 for x, y in zip(vec1, vec2))
    return distance
import unittest


class TestSquaredEuclideanDistance(unittest.TestCase):
    def test_standard_vectors(self):
        """Test squared distance calculation for typical vectors."""
        vec1 = [1, 2, 3]
        vec2 = [4, 5, 6]
        expected_result = 27  # (3^2 + 3^2 + 3^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_vectors_with_zeros(self):
        """Test vectors that include zero values."""
        vec1 = [0, 0, 0]
        vec2 = [0, 0, 0]
        expected_result = 0
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_vectors_with_negative_values(self):
        """Test vectors that include negative values."""
        vec1 = [-1, -2, -3]
        vec2 = [-4, -5, -6]
        expected_result = 27  # (3^2 + 3^2 + 3^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_single_element_vectors(self):
        """Test single element vectors."""
        vec1 = [5]
        vec2 = [-5]
        expected_result = 100  # (10^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()