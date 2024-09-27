import numpy as np


def apply_shear_x(matrix: np.array, shear_factor: float):
    """
    Applies a shear transformation to a 2D matrix along the x-axis.

    Args:
    matrix (np.ndarray): A 2D numpy array representing the original matrix.
    shear_factor (float): The factor by which the matrix is sheared along the x-axis.

    Returns:
    np.ndarray: The sheared matrix.
    """
