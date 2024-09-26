import numpy as np


def get_shear(matrix: np.array) -> float:
    """
    Given an affine matrix, return the corresponding shear.
    Written by ChatGPT
    """
    scale_x, scale_y = get_scale(matrix)
    shear = float(np.dot(matrix[:, 0], matrix[:, 1]) / (scale_x * scale_y))
    return shear
