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