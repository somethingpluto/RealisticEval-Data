import numpy as np

def get_rotation(matrix:np.array) -> float:
    """
    Given an affine transformation matrix, return the corresponding rotation angle in radians.

    Args:
        matrix (np.array): A 2D affine transformation matrix.

    Returns:
        float: The rotation angle in radians, extracted from the affine matrix.
    """