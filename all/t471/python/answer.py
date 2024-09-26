import numpy as np

def get_rotation(matrix:np.array) -> float:
    """
    Given an affine transformation matrix, return the corresponding rotation angle in radians.

    Args:
        matrix (np.array): A 2D affine transformation matrix.

    Returns:
        float: The rotation angle in radians, extracted from the affine matrix.
    """
    # Ensure the matrix is a 2D numpy array and has the correct shape
    if not isinstance(matrix, np.ndarray) or matrix.shape != (3, 3):
        raise ValueError("Input must be a 3x3 affine transformation matrix.")

    # Calculate the rotation angle using arctan2
    rotation_angle = np.arctan2(matrix[1, 0], matrix[0, 0])

    return float(rotation_angle)