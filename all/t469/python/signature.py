import numpy as np


def get_scale(matrix: np.ndarray) -> tuple[np.float64, np.float64]:
    """
    Given a 3x3 affine transformation matrix, return the corresponding scaling factors
    along the x and y axes.

    Args:
        matrix (np.ndarray): A 3x3 affine transformation matrix.

    Returns:
        tuple[np.float64, np.float64]: A tuple containing the scale factors (scale_x, scale_y).
    """