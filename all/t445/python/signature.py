import numpy
import numpy as np


def create_rot_matrix(angle_deg: float, axis: str) -> numpy.ndarray:
    """
    Create a pose matrix representing a rotation about a given axis.

    Args:
        angle_deg (float): Rotation angle in degrees.
        axis (str): Axis to rotate about, must be one of 'X', 'Y', or 'Z'.

    Returns:
        numpy.ndarray: 4x4 pose matrix representing the rotation.
    """
