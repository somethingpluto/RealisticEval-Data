import math


def quaternion_to_yaw(w:float, x:float, y:float, z:float) -> float:
    """
    The quaternion is converted to a selected yaw Angle around the z-axis
    Args:
        w (float): The scalar component of the quaternion.
        x (float): The x-component of the quaternion vector part.
        y (float): The y-component of the quaternion vector part.
        z (float): The z-component of the quaternion vector part.

    Returns: The yaw angle in radians.

    """