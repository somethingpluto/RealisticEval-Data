import numpy as np


def get_translation(matrix: np.array) -> np.typing.NDArray[np.float64]:
    """
    Given an affine matrix, return the corresponding translation.
    Written by ChatGPT
    """
    return matrix[:2, 2]
