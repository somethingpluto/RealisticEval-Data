import unittest

class TestSquaredEuclideanDistance(unittest.TestCase):
    def test_standard_vectors(self):
        """Test squared distance calculation for typical vectors."""
        vec1 = [1, 2, 3]
        vec2 = [4, 5, 6]
        expected_result = 27  # (3^2 + 3^2 + 3^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_vectors_of_different_lengths(self):
        """Test vectors of different lengths to ensure it raises ValueError."""
        vec1 = [1, 2, 3]
        vec2 = [1, 2]
        with self.assertRaises(ValueError):
            squared_euclidean_distance(vec1, vec2)

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
def squared_euclidean_distance(vec1, vec2):
    """
    Compute the squared Euclidean distance between two vectors.

    Args:
    vec1 (list or tuple): First vector.
    vec2 (list or tuple): Second vector.

    Returns:
    float: Squared Euclidean distance between vec1 and vec2.

    Raises:
    ValueError: If the vectors are of different lengths.
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length")

    distance_squared = sum((a - b) ** 2 for a, b in zip(vec1, vec2))
    return distance_squared