import math
from typing import Tuple


def quaternion_to_angle(quaternion: Tuple[float]) -> float:
    """
    Converts a quaternion to a rotation angle in radians.

    Args:
        quaternion (Tuple[float]): A tuple or list containing the quaternion components (w, x, y, z)

    Returns:
        float: The rotation angle in radians
    """
