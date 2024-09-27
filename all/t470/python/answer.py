import numpy as np

def apply_shear_x(matrix, shear_factor):
    """
    Applies a shear transformation to a 2D matrix along the x-axis.

    Args:
    matrix (np.ndarray): A 2D numpy array representing the original matrix.
    shear_factor (float): The factor by which the matrix is sheared along the x-axis.

    Returns:
    np.ndarray: The sheared matrix.
    """
    # Define the shear transformation matrix for shearing along the x-axis
    shear_matrix = np.array([[1, shear_factor],
                             [0, 1]])

    # Applying the shear transformation
    # For matrix multiplication, use np.dot() or @ operator
    transformed_matrix = matrix @ shear_matrix

    return transformed_matrix