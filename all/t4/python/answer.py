import math


def quaternion_to_yaw(w, x, y, z):
    """
    Convert a quaternion to a yaw angle around the z-axis.

    Parameters:
        w (float): The scalar component of the quaternion.
        x (float): The x-component of the quaternion vector part.
        y (float): The y-component of the quaternion vector part.
        z (float): The z-component of the quaternion vector part.

    Returns:
        float: The yaw angle in radians.
    """
    # Calculate the yaw (psi) using the atan2 function
    psi = math.atan2(2 * (w * z + x * y), 1 - 2 * (y ** 2 + z ** 2))
    return psi