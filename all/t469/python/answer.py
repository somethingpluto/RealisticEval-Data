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
    # Ensure the matrix is a 3x3 numpy array
    if not isinstance(matrix, np.ndarray) or matrix.shape != (3, 3):
        raise ValueError("Input must be a 3x3 affine transformation matrix.")

    # Calculate the scale factors using the norm of the columns
    scale_x = np.linalg.norm(matrix[0:2, 0])  # Using the first two rows for x-scale
    scale_y = np.linalg.norm(matrix[0:2, 1])  # Using the first two rows for y-scale

    return float(scale_x), float(scale_y)
