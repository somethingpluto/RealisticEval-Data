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

import numpy as np
from typing import Dict


def rotation_mapping_to_matrix(rotation_map: Dict[int, int]) -> np.ndarray:
    """
    Converts a rotation map specifying new indices for primary axis unit vectors into a rotation matrix.

    Parameters:
        rotation_map (dict[int, int]): A dictionary mapping original vector indices to new indices.

    Returns:
        np.ndarray: A 3x3 rotation matrix.

    Assumptions:
        - `RULE_ORDER` is defined as a list of numpy arrays representing the unit vectors along the x, y, and z axes.
        - `rotation_map` should map three unique input keys (representing x, y, z axes) to three unique output values in [0, 1, 2].
    """
    # Define unit vectors for x, y, z axes assuming standard basis vectors
    RULE_ORDER = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]

    # Initialize a 3x3 zero matrix
    rotation_matrix = np.zeros((3, 3))

    # Check if the rotation_map has valid mappings
    if sorted(rotation_map.keys()) != [0, 1, 2]:
        raise ValueError("Invalid keys in rotation_map. Keys must be 0, 1, 2.")
    if sorted(rotation_map.values()) != [0, 1, 2]:
        raise ValueError("Invalid values in rotation_map. Values must be 0, 1, 2 without repetition.")

    # Build the rotation matrix by placing the mapped vectors in the correct columns
    for original_index, new_index in rotation_map.items():
        rotation_matrix[:, original_index] = RULE_ORDER[new_index]

    # Validate that the constructed matrix is a valid rotation matrix by checking the determinant
    if not np.isclose(np.linalg.det(rotation_matrix), 1):
        raise ValueError(
            "The resulting matrix does not have a determinant of 1, which is required for a valid rotation matrix.")

    return rotation_matrix