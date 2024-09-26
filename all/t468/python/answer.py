import numpy as np


def get_translation(matrix: np.ndarray) -> np.ndarray:
    """
    Given a 3x3 matrix, return the corresponding translation vector.

    Args:
        matrix (np.ndarray): A 3x3 affine transformation matrix.

    Returns:
        np.ndarray: A 2-element array containing the translation components (translation_x, translation_y).
    """
    # Ensure the matrix is a 3x3 numpy array
    if not isinstance(matrix, np.ndarray) or matrix.shape != (3, 3):
        raise ValueError("Input must be a 3x3 affine transformation matrix.")

    # Extract the translation components from the matrix
    translation = matrix[:2, 2]

    return translation.astype(np.float64)  # Ensure the return type is float64