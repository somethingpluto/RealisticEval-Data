import numpy as np


def check_xor_sum(combination: np.ndarray):
    """
    Checks the XOR sums of specific columns in a given combination array.

    Args:
        combination (np.ndarray): A 2D numpy array where each column corresponds
                                  to a specific value.

    Returns:
        bool: True if the XOR sums of the specified columns match the required
              values; otherwise, False.
    """
