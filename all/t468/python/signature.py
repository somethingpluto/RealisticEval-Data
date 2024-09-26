import numpy as np


def get_translation(matrix: np.ndarray) -> np.ndarray:
    """
    Given a 3x3 matrix, return the corresponding translation vector.

    Args:
        matrix (np.ndarray): A 3x3 affine transformation matrix.

    Returns:
        np.ndarray: A 2-element array containing the translation components (translation_x, translation_y).
    """