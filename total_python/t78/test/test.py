import unittest
import numpy as np


# Assuming the function rotation_mapping_to_matrix is defined as described above
class TestRotationMappingToMatrix(unittest.TestCase):
    def test_valid_rotation(self):
        """Test a valid rotation mapping."""
        rotation_map = {0: 2, 1: 0, 2: 1}  # An example of a valid rotation
        expected_matrix = np.array([[0, 0, 1],
                                    [1, 0, 0],
                                    [0, 1, 0]])
        result_matrix = rotation_mapping_to_matrix(rotation_map)
        np.testing.assert_array_almost_equal(result_matrix, expected_matrix)

    def test_invalid_keys(self):
        """Test rotation mapping with invalid keys."""
        rotation_map = {0: 2, 1: 0, 3: 1}  # Key 3 is invalid
        with self.assertRaises(ValueError):
            rotation_mapping_to_matrix(rotation_map)

    def test_invalid_values(self):
        """Test rotation mapping with invalid values."""
        rotation_map = {0: 2, 1: 0, 2: 3}  # Value 3 is out of allowed range [0, 1, 2]
        with self.assertRaises(ValueError):
            rotation_mapping_to_matrix(rotation_map)

    def test_identity_rotation(self):
        """Test the identity rotation mapping."""
        rotation_map = {0: 0, 1: 1, 2: 2}
        expected_matrix = np.eye(3)
        result_matrix = rotation_mapping_to_matrix(rotation_map)
        np.testing.assert_array_almost_equal(result_matrix, expected_matrix)

    def test_reverse_rotation(self):
        """Test reversing two axes."""
        rotation_map = {0: 1, 1: 0, 2: 2}
        expected_matrix = np.array([[0, 1, 0],
                                    [1, 0, 0],
                                    [0, 0, 1]])
        result_matrix = rotation_mapping_to_matrix(rotation_map)
        np.testing.assert_array_almost_equal(result_matrix, expected_matrix)
