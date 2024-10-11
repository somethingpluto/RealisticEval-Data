import math


def quaternion_to_angle(quaternion):
    """
    Converts a quaternion to a rotation angle in radians.

    :param quaternion: A tuple or list containing the quaternion components (w, x, y, z)
    :return: The rotation angle in radians
    """
    # Ensure the quaternion is a valid 4-element tuple or list
    if len(quaternion) != 4:
        raise ValueError("Quaternion must have 4 components (w, x, y, z)")

    w, x, y, z = quaternion

    # Calculate the angle in radians
    angle = 2 * math.acos(w)

    return angle
